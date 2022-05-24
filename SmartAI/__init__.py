import paho.mqtt.client as mqtt
import pymysql
from flask import Flask, render_template 
import numpy as np


app = Flask(__name__)
app.debug = True
 
broker_address = '192.168.10.84'
broker_port = 1883
led_topic = 'inTopic'
led_topic2 = 'inTopic2'
led_topic3 = 'inTopic3'


mqtt=mqtt.Client()
mqtt.connect(broker_address,broker_port,60)



mqtt.loop_start()

def db_connector():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234qwer', db='SmartAI', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT student_name FROM SmartAI.students;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)
 

@app.route('/test')
def index():
    a = db_connector()
    return a

@app.route("/")
def main():
 return render_template('sample.html')
 
@app.route("/led_on")
def action_led_on():
   mqtt.publish(led_topic,"1")
   return render_template('sample.html')

@app.route("/led_off")
def action_led_off():
   mqtt.publish(led_topic,"0")
   return render_template('sample.html')

@app.route("/led_on2")
def action_led_on2():
   mqtt.publish(led_topic2,"1")
   return render_template('sample.html')

@app.route("/led_off2")
def action_led_off2():
   mqtt.publish(led_topic2,"0")
   return render_template('sample.html')

@app.route("/led_on3")
def action_led_on3():
   mqtt.publish(led_topic3,"1")
   return render_template('sample.html')

@app.route("/led_off3")
def action_led_off3():
   mqtt.publish(led_topic3,"0")
   return render_template('sample.html')


