from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(logger=True, engineio_logger=True)


def create_app(debug = False):
    
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = '1234qwer'
    
    socketio.init_app(app)
    
    #from.import acuator_control
    from . import API_db
    from . import routes
    from . import test
    from . import socket_event
    
    #app.register_blueprint(acuator_control.blue_control)
    app.register_blueprint(API_db.blue_api)
    app.register_blueprint(routes.blue_index)
    app.register_blueprint(test.blue_test)
    app.register_blueprint(socket_event.blue_socket)
    
    from .socket_event import socketio_init
    socketio_init(socketio)
      
    return app

