import random
from paho.mqtt import client as mqtt
import mysql.connector as mariadb


broker = '192.168.10.84'
port = 1883
topic = "outTopic"
topic2 = "outTopic2"

mariadb_connection = mariadb.connect(
    host='localhost',
    user='root', 
    password='1234qwer', 
    database='SmartAI')

cursor = mariadb_connection.cursor()

def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        sql = "INSERT INTO Test (topic, payload) VALUES(%s, %s)"
        val = [(msg.topic), (msg.payload)]
        cursor.execute(sql,val)
        mariadb_connection.commit()

    client.subscribe(topic)
    client.subscribe(topic2)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
