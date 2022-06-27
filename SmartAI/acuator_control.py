from flask import Blueprint,request

from SmartAI.module import mqttModule

blue_control = Blueprint("control", __name__)

topic={'led':'intopic',
      'fan':'actuator/fan',
      'solenoidvalve':'actuator/solenoidvalve',
      'doorlook':'actuator/doorlook',
      'switch':'actuator/switch'
}

mqtt = mqttModule.Mqtt_Broker()

'''LED'''
@blue_control.route("/led/on", methods=['GET'])
def led_on():
   result=mqtt.topic_publish(topic['led'],"1")
   return result
       
@blue_control.route("/led/off", methods=['GET'])
def led_off():
   result=mqtt.topic_publish(topic['led'],"0")
   return result

'''FAN'''
@blue_control.route("/fan/on", methods=['GET'])
def fan_on():
   result=mqtt.topic_publish(topic['fan'],"1")
   return result


@blue_control.route("/fan/off", methods=['GET'])
def fan_off():
   result=mqtt.topic_publish(topic['fan'],"0")
   return result

'''Solenoid Valve'''
@blue_control.route("/solenoid/on", methods=['GET'])
def solenoid_on():
   result=mqtt.topic_publish(topic['solenoidvalve'],"1")
   return result


@blue_control.route("/solenoid/off", methods=['GET'])
def solenoid_off():
   result=mqtt.topic_publish(topic['solenoidvalve'],"0")
   return result

'''Door Lock'''
@blue_control.route("/doorlock/on", methods=['GET'])
def doorlock_on():
   result=mqtt.topic_publish(topic['doorlook'],"1")
   return result


@blue_control.route("/doorlock/off", methods=['GET'])
def doorlock_off():
   result=mqtt.topic_publish(topic['doorlook'],"0")
   return result

'''button'''
@blue_control.route("/button/on", methods=['GET'])
def button_on():
   result=mqtt.topic_publish(topic['switch'],"1")
   return result


@blue_control.route("/button/off", methods=['GET'])
def button_off():
   result=mqtt.topic_publish(topic['switch'],"0")
   return result
