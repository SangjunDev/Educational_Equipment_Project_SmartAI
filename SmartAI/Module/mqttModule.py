import paho.mqtt.client as mqtt


broker_address = '192.168.10.85'
broker_port = 1883


class Mqtt_Broker():
    def __init__(self):
        self.mqtt=mqtt.Client()
        self.mqtt.connect(broker_address,broker_port,60)
        self.mqtt.loop_start()
        
        
    def Control_publish(self,topic,payload,args={}):
        try:
            self.mqtt.publish(topic,payload)
            return "OK"       
        except:
            return "FAIL"