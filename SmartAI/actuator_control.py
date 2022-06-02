from ast import Expression
from flask import Blueprint, render_template ,request
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

@blue_control.route("/led/on")
def led1_on():
   try:
      mqtt.publish(led_topic,"1")
      return "OK"
   except:
      return "FAIL"


@blue_control.route("/led/off")
def led1_off():
   try:   
      mqtt.publish(led_topic,"0")
      return "OK"
   except :
        return "FAIL"


@blue_control.route("/led2/on")
def led2_on():
   try:
      mqtt.publish(led_topic2,"1")
      return "OK"
   except:
      return "FAIL"


@blue_control.route("/led2/off")
def led2_off():
   try:   
      mqtt.publish(led_topic2,"0")
      return "OK"
   except :
        return "FAIL"

@blue_control.route("/led3/on")
def led3_on():
   try:   
    mqtt.publish(led_topic3,"0")
    return "OK"
   except :
        return "FAIL"


@blue_control.route("/led3/off")
def led3_off():
   try:   
      mqtt.publish(led_topic3,"0")
      return "OK"
   except :
        return "FAIL"
