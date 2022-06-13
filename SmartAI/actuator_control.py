from flask import Blueprint,request
import paho.mqtt.client as mqtt

from SmartAI.module import mqttModule

blue_control = Blueprint("control", __name__)

led_topic = 'inTopic'
led_topic2 = 'inTopic2'
led_topic3 = 'LED/Control'


@blue_control.route("/led/on", methods=['GET'])
def led1_on():
   led2_mqtt = mqttModule.Mqtt_Broker()
   result=led2_mqtt.Control_publish(led_topic,"1")
   return result
       


@blue_control.route("/led/off", methods=['GET'])
def led1_off():
   led2_mqtt = mqttModule.Mqtt_Broker()
   result=led2_mqtt.Control_publish(led_topic,"0")
   return result


@blue_control.route("/led2/on", methods=['GET'])
def led2_on():
   led2_mqtt = mqttModule.Mqtt_Broker()
   result=led2_mqtt.Control_publish(led_topic2,"1")
   return result


@blue_control.route("/led2/off", methods=['GET'])
def led2_off():
   led2_mqtt = mqttModule.Mqtt_Broker()
   result=led2_mqtt.Control_publish(led_topic2,"0")
   return result

@blue_control.route("/led3/on", methods=['GET'])
def led3_on():
   led2_mqtt = mqttModule.Mqtt_Broker()
   result=led2_mqtt.Control_publish(led_topic3,"1")
   return result


@blue_control.route("/led3/off", methods=['GET'])
def led3_off():
   led2_mqtt = mqttModule.Mqtt_Broker()
   result=led2_mqtt.Control_publish(led_topic3,"0")
   return result
