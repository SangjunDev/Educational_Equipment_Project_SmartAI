import paho.mqtt.client as mqtt


broker_address = '192.168.10.85'
broker_port = 1883


class Mqtt_Broker():
    def __init__(self):
        self.mqtt=mqtt.Client()
        self.mqtt.connect(broker_address,broker_port)
        self.mqtt.loop_start()
        
        
    def topic_publish(self,topic,payload):
        try:
             self.mqtt.publish(topic,payload)
             self.mqtt.loop_stop()
             return "OK"
        except:
            self.mqtt.loop_stop()
            return "FAIL"
