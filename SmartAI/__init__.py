from flask import Flask,render_template
from flask_socketio import SocketIO, send

from.import acuator_control
from.import API_db
from.import index
from.import test

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234qwer'
socketio=SocketIO(app)


    
app.register_blueprint(acuator_control.blue_control)
app.register_blueprint(API_db.blue_api)
app.register_blueprint(index.blue_index)
app.register_blueprint(test.blue_test)



