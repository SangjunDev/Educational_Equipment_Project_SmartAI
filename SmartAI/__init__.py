from flask import Flask, render_template 
from . import control 
from . import read_db
from . import index

app = Flask(__name__)

app.register_blueprint(control.blue_control)
app.register_blueprint(read_db.blue_read)
app.register_blueprint(index.blue_index)
 

 



