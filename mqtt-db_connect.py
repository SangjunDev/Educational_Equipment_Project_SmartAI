import time
import threading
import logging
import atexit
from paho.mqtt import client as mqtt
import mysql.connector as mariadb


broker = '192.168.10.84'
port = 1883
topic = ["outTopic", "outTopic2"]

mariadb_connection = mariadb.connect(
    host='localhost',
    user='root', 
    password='1234qwer', 
    database='SmartAI')

cursor = mariadb_connection.cursor()

def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            #logging.info("Connected to MQTT Broker!")
            print("Connected to MQTT Broker!")
        else:
            #logging.info("Failed to connect, return code %d\n", rc)
            print("Connected to MQTT Broker!")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        #logging.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        sql = "INSERT INTO Test (topic, payload) VALUES(%s, %s)"
        val = [(msg.topic), (msg.payload)]
        cursor.execute(sql,val)
        mariadb_connection.commit()
    
    for topics in topic:
     client.subscribe(topics)
    #client.subscribe(topic2)
    client.on_message = on_message
    

def db_truncate():
    sql = "TRUNCATE Test;"
    cursor.execute(sql)
    mariadb_connection.commit()

def run():
    client = connect_mqtt()
    subscribe(client)
    time.sleep(2)    
    #t=threading.Thread(target = subscribe, args = client)
    #t.daemon = True
    #t.start()
    client.loop_forever()
    


if __name__ == '__main__':
    
    try:
     atexit.register(db_truncate)
     run()
    except :
        exit()
        
