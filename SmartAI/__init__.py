from flask import Flask
from.import MQTT_control
from.import API_db
from.import index
from.import test



app = Flask(__name__)


app.register_blueprint(MQTT_control.blue_control)
app.register_blueprint(API_db.blue_api)
app.register_blueprint(index.blue_index)
app.register_blueprint(test.blue_test)



