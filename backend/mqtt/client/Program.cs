using System;
using System.Collections.Generic;
using System.Threading.Tasks;
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
        private const int MqttPort = 707;
        private const string ServerIp = "localhost";


        // cache list
        public static bool isConnected;
        public static List<string> cache = new List<string>();

        //silos & zone id
        private const string silosId = "silosId";
        private const string zoneId = "zoneId";
        public static void OnConnected(MqttClientConnectedEventArgs obj)
        {
            Log.Logger.Information("Successfully connected.");
            isConnected = true;
        }

        public static void OnConnectingFailed(ManagedProcessFailedEventArgs obj)
        {
            Log.Logger.Warning("Couldn't connect to broker.");
            isConnected = false;
        }

        public static void OnDisconnected(MqttClientDisconnectedEventArgs obj)
        {
            Log.Logger.Information("Successfully disconnected.");
        }

        static void Main(string[] args)
        {
            Task.Delay(2000).GetAwaiter().GetResult();
            // Creates a new client
            MqttClientOptionsBuilder builder = new MqttClientOptionsBuilder()
                                                .WithClientId(zoneId)
                                                .WithTcpServer(ServerIp, MqttPort);

            // Create client options objects
            ManagedMqttClientOptions options = new ManagedMqttClientOptionsBuilder()
                                    .WithAutoReconnectDelay(TimeSpan.FromSeconds(10))
                                    .WithClientOptions(builder.Build())
                                    .Build();

            // Creates the client object
            IManagedMqttClient _mqttClient = new MqttFactory().CreateManagedMqttClient();

            // Set up handlers
            _mqttClient.ConnectedHandler = new MqttClientConnectedHandlerDelegate(OnConnected);
            _mqttClient.DisconnectedHandler = new MqttClientDisconnectedHandlerDelegate(OnDisconnected);
            _mqttClient.ConnectingFailedHandler = new ConnectingFailedHandlerDelegate(OnConnectingFailed);

            // Starts a connection with the Broker
            _mqttClient.StartAsync(options).GetAwaiter().GetResult();

            //crea json da inviare
            string json = JsonConvert.SerializeObject(new { message = "numSensoriAttivi", sent = DateTimeOffset.UtcNow });

            // se è connesso al server mqtt e ci sono dati in cache prima manda la cache, poi l'ultimo report
            if (isConnected)
            {
                if (cache.Count > 0)
                {
                    foreach (var item in cache)
                    {
                        _mqttClient.PublishAsync(silosId, item);
                    }
                    cache.Clear();
                }
                _mqttClient.PublishAsync(silosId, json);
            }

            // se non è connesso al server salva in una lista 
            else
            {
                cache.Add(json);
            }
        }
    }
}