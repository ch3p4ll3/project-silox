using System;
using System.Text;
using MQTTnet;
using MQTTnet.Server;
using Serilog;

namespace mqtt
{
    internal class Server
    {
        private static int MessageCounter = 0;
        private static IMqttServer mqttServer;

        public static void OnNewConnection(MqttConnectionValidatorContext context)
        {
            Log.Logger.Information(
                    "New connection: ClientId = {clientId}, Endpoint = {endpoint}",
                    context.ClientId,
                    context.Endpoint);
        }

        public static void OnNewMessage(MqttApplicationMessageInterceptorContext context)
        {
            var payload = context.ApplicationMessage?.Payload == null ? null : Encoding.UTF8.GetString(context.ApplicationMessage?.Payload);

            MessageCounter++;

            Console.WriteLine($"MessageId: {MessageCounter} - TimeStamp: {DateTime.Now} -- Message: ClientId = {context.ClientId}, Topic = {context.ApplicationMessage?.Topic}, Payload = {payload}, QoS = {context.ApplicationMessage?.QualityOfServiceLevel}, Retain-Flag = {context.ApplicationMessage?.Retain}");
            //mqttServer.PublishAsync("info", "aggiorna");
        }
        static void Main(string[] args)
        {
            MqttServerOptionsBuilder options = new MqttServerOptionsBuilder()
                                     // set endpoint to localhost
                                     .WithDefaultEndpoint()
                                     // port used will be 707
                                     .WithDefaultEndpointPort(707)
                                     .WithClientId("server")
                                     // handler for new connections
                                     .WithConnectionValidator(OnNewConnection)
                                     // handler for new messages
                                     .WithApplicationMessageInterceptor(OnNewMessage);

            // creates a new mqtt server     
            mqttServer = new MqttFactory().CreateMqttServer();

            // start the server with options
            mqttServer.StartAsync(options.Build()).GetAwaiter().GetResult();

            // keep application running until user press a key
            Console.WriteLine("Server started");
            Console.ReadLine();
        }
    }
}
