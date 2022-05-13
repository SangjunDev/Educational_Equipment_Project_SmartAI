import paho.mqtt.client as mqtt

mqttc=mqtt.Client("Test_Client")
mqttc.connect("192.168.10.84",1883)

mqttc.publish("inTopic","0")
 
    