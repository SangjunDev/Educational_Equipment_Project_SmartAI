from flask import Blueprint,request, render_template
from flask_socketio import SocketIO, send, emit
from SmartAI.__init__ import socketio

import json

from SmartAI.module import mqttModule

blue_test = Blueprint("test", __name__)

led_topic2 = 'inTopic2'


@blue_test.route("/test3",methods=["GET","POST"])
def main5():
    value = request.form['SensorID']
    
    jsondata=json.dumps(request.form['SensorID'])   
    
    return jsondata , str(value)

@blue_test.route("/test4",methods=["GET","POST"])
def main3():

    return render_template('test/annya.html')

@blue_test.route('/socket')

@socketio.on('message')
def handle_message(message):
    send(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
    
    
    
    
