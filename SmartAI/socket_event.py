from argparse import Namespace
from flask import Blueprint
from flask_socketio import emit,disconnect



from SmartAI.module import dbModule

blue_socket = Blueprint("socket", __name__)

sql = { 'illuminace' : 'SELECT payload,time(real_t) FROM ILLUMINANCE ORDER BY id DESC LIMIT 1',
        'gas': 'SELECT payload,time(real_t) FROM GAS ORDER BY id DESC LIMIT 1',
        'temp': 'SELECT payload_t,payload_h,time(real_t) FROM TEMP ORDER BY id DESC LIMIT 1',
        'dust': 'SELECT payload,time(real_t) FROM DUST ORDER BY id DESC LIMIT 1',
        'pir': 'SELECT payload,time(real_t) FROM PIR ORDER BY id DESC LIMIT 1'
}



def raedTable(query, args={}):
    db = dbModule.Database()
    row = db.executeAll(query, args={})
    return row



def socketio_init(socketio):
    
    #@socketio.on('connect', namespace='/sockettest')
    #def connect():
       # data = "connect"
        #emit("response", data)
        
   # @socketio.on('disconnect', namespace='/sockettest')
   # def disconnect():
        #print("disconnected")         
    
    @socketio.on('request', namespace='/sockettest')
    def request(message):
        to_client = dict()
        
        if message == 'connect':
            while(1): 
                message = raedTable(sql['temp'])
                print(message)
                to_client['temp'] = message[0][0]
                to_client['humi'] = message[0][1]
                to_client['time'] = str(message[0][2])
                to_client['type'] = 'data'
                emit('response',to_client, broadcast = True) 
                socketio.sleep(5)
        else:
            pass          
        
                                   
    @socketio.on_error() 
    def error_handler(e):
        pass
    
    @socketio.on_error_default 
    def default_error_handler(e):
        pass