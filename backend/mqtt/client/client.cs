using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using MQTTnet;
using MQTTnet.Client.Connecting;
using MQTTnet.Client.Disconnecting;
using MQTTnet.Client.Options;
using MQTTnet.Extensions.ManagedClient;
using Newtonsoft.Json;
using Serilog;
using Spectre.Console;


namespace mqtt
{
    internal class Client
    {
        // mqtt server config
        private const int MqttPort = 707;
        private const string ServerIp = "localhost";
        private static IManagedMqttClient _mqttClient;
        private const int retryTimeout = 10;

        // silos & zone id
        private static string silosId = "silosId";
        private static string zoneId = "zoneId";

        // info silos
        private static int livello = 0;
        private static int livelloMax = 8;
        public static void OnConnected(MqttClientConnectedEventArgs obj)
        {
            Log.Logger.Information("Successfully connected.");
        }

        public static void OnConnectingFailed(ManagedProcessFailedEventArgs obj)
        {
            Log.Logger.Warning("Couldn't connect to broker.");
        }

        public static void OnDisconnected(MqttClientDisconnectedEventArgs obj)
        {
            Log.Logger.Information("Successfully disconnected.");
        }

        public static void OnMessage(MqttApplicationMessageReceivedEventArgs e)
        {
            Console.WriteLine($"+ Payload = {Encoding.UTF8.GetString(e.ApplicationMessage.Payload)}");
        }

        static void Main(string[] args)
        {
            bool run = true;
            while (true) {
                string silos = getSilos();
                silosId = silos.Split('-')[1];
                zoneId = silos.Split('-')[0];

                updateSilosInfo();

                while (run)
                {
                    var azione = AnsiConsole.Prompt(
                        new SelectionPrompt<string>()
                            .Title("Cosa vuoi fare?")
                            .PageSize(10)
                            .AddChoices(new[] {
                            "Riempi", "Scarica", "indietro",
                    }));

                    switch (azione)
                    {
                        case "indietro":
                            run = false;
                            break;

                        case "Riempi":
                            if (livello < livelloMax)
                                sendMsg(++livello);
                            break;

                        case "Scarica":
                            if (livello > 0)
                                sendMsg(--livello);
                            break;
                    }
                }
                run = true;
            }
        }

        private static void sendMsg(int sensoriAttivi)
        {
            //crea json da inviare
            string json = JsonConvert.SerializeObject(new { message = sensoriAttivi, sent = DateTimeOffset.UtcNow });

            _mqttClient.PublishAsync(silosId, json);
        }

        // prendi silos da db per selezionarlo 
        private static string getSilos()
        {
            var silos = AnsiConsole.Prompt(
                        new SelectionPrompt<string>()
                            .Title("Seleziona Silos")
                            .PageSize(10)
                            .AddChoices(new[] {
                            "Idzona1-idSilos1", "Idzona2-idSilos2", "esci",
                    }));

            if (silos == "esci")
            {
                System.Environment.Exit(0);
            }
            return silos;
        }

        //dopo aver selezionato il nuovo silos aggiorna le info per mqtt e aggiorna lo stato attuale
        public static void updateSilosInfo()
        {
            livello = 0;
            // Creates a new client
            MqttClientOptionsBuilder builder = new MqttClientOptionsBuilder()
                                                .WithClientId(zoneId)
                                                .WithTcpServer(ServerIp, MqttPort);

            // Create client options objects
            ManagedMqttClientOptions options = new ManagedMqttClientOptionsBuilder()
                                    .WithAutoReconnectDelay(TimeSpan.FromSeconds(retryTimeout))
                                    .WithClientOptions(builder.Build())
                                    .Build();

            // Creates the client object
            _mqttClient = new MqttFactory().CreateManagedMqttClient();
            _mqttClient.SubscribeAsync("info");

            // Set up handlers
            _mqttClient.ConnectedHandler = new MqttClientConnectedHandlerDelegate(OnConnected);
            _mqttClient.DisconnectedHandler = new MqttClientDisconnectedHandlerDelegate(OnDisconnected);
            _mqttClient.ConnectingFailedHandler = new ConnectingFailedHandlerDelegate(OnConnectingFailed);
            _mqttClient.UseApplicationMessageReceivedHandler(OnMessage);

            // Starts a connection with the Broker
            _mqttClient.StartAsync(options).GetAwaiter().GetResult();
        }
    }
}