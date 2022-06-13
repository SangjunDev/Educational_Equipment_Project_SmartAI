from flask import Flask
from.import actuator_control
from.import read_db
from.import index
from.import graph


app = Flask(__name__)


app.register_blueprint(actuator_control.blue_control)
app.register_blueprint(read_db.blue_read)
app.register_blueprint(index.blue_index)
app.register_blueprint(graph.blue_index)


