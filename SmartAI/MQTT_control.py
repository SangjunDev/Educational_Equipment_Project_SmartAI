from flask import Blueprint,request
import paho.mqtt.client as mqtt

from SmartAI.module import mqttModule

blue_control = Blueprint("control", __name__)

led_topic = 'inTopic'
led_topic2 = 'inTopic2'
led_topic3 = 'LED/Control'


'''LED'''
@blue_control.route("/led/on", methods=['GET'])
def led_on():
   led_mqtt = mqttModule.Mqtt_Broker()
   result=led_mqtt.Control_publish(led_topic2,"1")
   return result
       
@blue_control.route("/led/off", methods=['GET'])
def led_off():
   led_mqtt = mqttModule.Mqtt_Broker()
   result=led_mqtt.Control_publish(led_topic2,"0")
   return result

'''FAN'''
@blue_control.route("/fan/on", methods=['GET'])
def fan_on():
   fan_mqtt = mqttModule.Mqtt_Broker()
   result=fan_mqtt.Control_publish(led_topic2,"1")
   return result


@blue_control.route("/fan/off", methods=['GET'])
def fan_off():
   fan_mqtt = mqttModule.Mqtt_Broker()
   result=fan_mqtt.Control_publish(led_topic2,"0")
   return result

'''Solenoid Valve'''
@blue_control.route("/solenoid/on", methods=['GET'])
def solenoid_on():
   solenoid_mqtt = mqttModule.Mqtt_Broker()
   result=solenoid_mqtt.Control_publish(led_topic3,"1")
   return result


@blue_control.route("/solenoid/off", methods=['GET'])
def solenoid_off():
   solenoid_mqtt = mqttModule.Mqtt_Broker()
   result=solenoid_mqtt.Control_publish(led_topic3,"0")
   return result

'''Door Lock'''
@blue_control.route("/doorlock/on", methods=['GET'])
def doorlock_on():
   doorlock_mqtt = mqttModule.Mqtt_Broker()
   result=doorlock_mqtt.Control_publish(led_topic3,"1")
   return result


@blue_control.route("/doorlock/off", methods=['GET'])
def doorlock_off():
   doorlock_mqtt = mqttModule.Mqtt_Broker()
   result=doorlock_mqtt.Control_publish(led_topic3,"0")
   return result

'''button'''
@blue_control.route("/button/on", methods=['GET'])
def button_on():
   button_mqtt = mqttModule.Mqtt_Broker()
   result=button_mqtt.Control_publish(led_topic3,"1")
   return result


@blue_control.route("/button/off", methods=['GET'])
def button_off():
   button_mqtt = mqttModule.Mqtt_Broker()
   result=button_mqtt.Control_publish(led_topic3,"0")
   return result
