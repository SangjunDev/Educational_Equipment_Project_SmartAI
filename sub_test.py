
import paho.mqtt.client as mqtt

#서버로부터 CONNTACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
	client.subscribe("outTopic3")

#서버로부터 publish message를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload)) 
 
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 

client.connect("192.168.10.84", 1883, 60) #라즈베리파이3 MQTT 
client.loop_forever()


