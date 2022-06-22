from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(logger=True, engineio_logger=True)

def create_app(debug = False):
    
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = '1234qwer'
    
    socketio.init_app(app)
    
    #from.import acuator_control
    from.import API_db
    from.import routes
    from.import test
    
    #app.register_blueprint(acuator_control.blue_control)
    app.register_blueprint(API_db.blue_api)
    app.register_blueprint(routes.blue_index)
    app.register_blueprint(test.blue_test)
    
    return app



