import paho.mqtt.client as mqtt
import os
import time
from threading import Thread
from flask import Flask, render_template, request



app = Flask(__name__)

broker_address = '192.168.10.84'
broker_port = 1883
led_topic = 'inTopic'
led_topic2 = 'inTopic2'
led_topic3 = 'inTopic3'

def on_connect(mqttc, userdata, rc):
 mqttc.subscribe("outTopic")

def on_message(mqttc, userdata, msg):
 print(msg.topic+" "+str(msg.payload))
 
mqttc=mqtt.Client()
mqttc.connect(broker_address,broker_port,60)

mqttc.loop_start()

@app.route("/")
def main():
 return render_template('sample.html')
 
@app.route("/led_on")
def action_led_on():
   mqttc.publish(led_topic,"1")
  
   return render_template('sample.html')

@app.route("/led_off")
def action_led_off():
   mqttc.publish(led_topic,"0")
   
   return render_template('sample.html')

@app.route("/led_on2")
def action_led_on2():
   mqttc.publish(led_topic2,"1")
   
   return render_template('sample.html')

@app.route("/led_off2")
def action_led_off2():
   mqttc.publish(led_topic2,"0")
   
   return render_template('sample.html')

@app.route("/led_on3")
def action_led_on3():
   mqttc.publish(led_topic3,"1")
   
   return render_template('sample.html')

@app.route("/led_off3")
def action_led_off3():
   mqttc.publish(led_topic3,"0")
   
   return render_template('sample.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True) 
