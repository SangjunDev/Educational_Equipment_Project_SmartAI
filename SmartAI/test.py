from turtle import Turtle
from flask import Blueprint,request,render_template
from flask_socketio import emit, disconnect


from SmartAI.module import dbModule

import json


from SmartAI.module import mqttModule

blue_test = Blueprint("test", __name__)

sql = { 'illuminace' : 'SELECT payload FROM ILLUMINANCE ORDER BY id DESC LIMIT 1',
        'gas': 'SELECT payload FROM GAS ORDER BY id DESC LIMIT 1',
        'temp': 'SELECT payload_t,payload_h FROM TEMP ORDER BY id DESC LIMIT 1',
        'dust': 'SELECT payload FROM DUST ORDER BY id DESC LIMIT 1',
        'pir': 'SELECT payload FROM PIR ORDER BY id DESC LIMIT 1'
}

def raedTable(query, args={}):
    db = dbModule.Database()
    row = db.executeAll(query, args={})
    return row
    


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
def main4():
        return render_template('test/test3.html')




                
                
    
