from flask import Blueprint, render_template 
import paho.mqtt.client as mqtt

blue_control = Blueprint("control", __name__)

broker_address = '192.168.10.85'
broker_port = 1883
led_topic = 'inTopic'
led_topic2 = 'inTopic2'
led_topic3 = 'inTopic3'


mqtt=mqtt.Client()
mqtt.connect(broker_address,broker_port,60)
mqtt.loop_start()

@blue_control.route("/led_on")
def action_led_on():
   mqtt.publish(led_topic,"1")
   return render_template('sample.html')

@blue_control.route("/led_off")
def action_led_off():
   mqtt.publish(led_topic,"0")
   return render_template('sample.html')

@blue_control.route("/led_on2")
def action_led_on2():
   mqtt.publish(led_topic2,"1")
   return render_template('sample.html')

@blue_control.route("/led_off2")
def action_led_off2():
   mqtt.publish(led_topic2,"0")
   return render_template('sample.html')

@blue_control.route("/led_on3")
def action_led_on3():
   mqtt.publish(led_topic3,"1")
   return render_template('sample.html')

@blue_control.route("/led_off3")
def action_led_off3():
   mqtt.publish(led_topic3,"0")
   return render_template('sample.html')