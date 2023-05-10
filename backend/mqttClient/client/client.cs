using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using client;
using MQTTnet;
using MQTTnet.Client.Connecting;
using MQTTnet.Client.Disconnecting;
using MQTTnet.Client.Options;
using MQTTnet.Extensions.ManagedClient;
using Newtonsoft.Json;
using Serilog;


namespace mqtt
{
    internal class Client
    {
        // mqtt server config
        private const int MqttPort = 1883;
        private const string ServerIp = "localhost";
        private static IManagedMqttClient _mqttClient;
        private const int retryTimeout = 10;
        static Dictionary<string, string> openWith = new Dictionary<string, string>();

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
            Console.WriteLine(Encoding.UTF8.GetString(e.ApplicationMessage.Payload));
        }

        static void Main(string[] args)
        {
            connect();

            while(true)
            {
                Misurazioni measur = getRandomMeasurement();
                sendMsg($"silos-{measur.idSilos}", measur);
                Thread.Sleep(5000);
            }
        }

        private static void sendMsg(string location, Misurazioni misurazione)
        {
            //crea json da inviare
            string json = JsonConvert.SerializeObject(misurazione);

            Console.WriteLine(json);

            _mqttClient.PublishAsync(location, json).Wait();
        }

        //dopo aver selezionato il nuovo silos aggiorna le info per mqtt e aggiorna lo stato attuale
        public static void connect()
        {
            // Creates a new client
            MqttClientOptionsBuilder builder = new MqttClientOptionsBuilder()
                                                .WithClientId("mqttClient#1")   
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

        public static void disconnect()
        {
            _mqttClient.StopAsync();
            _mqttClient.Dispose();
        }

        public static Misurazioni getRandomMeasurement()
        {
            Random rnd = new Random();

            Misurazioni misurazioni = new Misurazioni()
            {
                idSilos = rnd.Next(1, 3),
                ph = rnd.Next(0, 13),
                tempInt = Math.Round(rnd.NextDouble(20.0, 35.0), 2),
                tempEst = Math.Round(rnd.NextDouble(-10.0, 40.0), 2),
                umiditaInt = Math.Round(rnd.NextDouble(0, 100), 2),
                umiditaEst = Math.Round(rnd.NextDouble(0, 100), 2),
                pressioneInt = Math.Round(rnd.NextDouble(0, 3), 2),
                livelloSensore1 = Math.Round(rnd.NextDouble(0, 8), 2),
                livelloSensore2 = Math.Round(rnd.NextDouble(0, 8), 2),
                livelloSensore3 = Math.Round(rnd.NextDouble(0, 8), 2),
                oraInvio = DateTime.Now
            };

            return misurazioni;
        }
    }

    public static class RandomExtensions
    {
        public static double NextDouble(
            this Random random,
            double minValue,
            double maxValue)
        {
            return random.NextDouble() * (maxValue - minValue) + minValue;
        }
    }
}