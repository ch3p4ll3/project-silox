from mqtt_listener import MqttListener


if __name__ == '__main__':
    a = None
    try:
        a = MqttListener()
        a.run()
    except:
        a.protocol.client.loop_stop()
        a.protocol.client.disconnect()