from mqtt_listener import MqttListener


if __name__ == '__main__':
    a = None
    try:
        a = MqttListener()  # create an instance of the class MqttListener
        a.run()  # run the instance
    except Exception as e:
        print(e)
        a.protocol.client.loop_stop()  # stop the loop of the mqtt client if an exception occurs
        a.protocol.client.disconnect()  # and disconnect the client from the broker
