from flask import Blueprint
from flask_socketio import emit
from SmartAI.module import dbModule as db

blue_socket = Blueprint("socket", __name__)

def socketio_init(socketio):
    
    @socketio.on('request', namespace='/sockettest')
    def request(message):
        to_client = dict()
        
        if message == 'connect':
            while(1): 
                message = db.raedData(db.socketSql['temp'])
                print(message)
                to_client['temp'] = message[0][0]
                to_client['humi'] = message[0][1]
                to_client['time'] = str(message[0][2])
                to_client['type'] = 'data'
                emit('response',to_client, broadcast = False) 
                socketio.sleep(5)
        else:
            pass          
        
                                   
    @socketio.on_error() 
    def error_handler(e):
        pass
    
    @socketio.on_error_default 
    def default_error_handler(e):
        pass