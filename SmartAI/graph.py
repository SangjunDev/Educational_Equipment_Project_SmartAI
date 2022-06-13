from flask import Blueprint, Response, make_response, render_template
from time import time
import json
import psutil


from SmartAI.module import dbModule

blue_index = Blueprint("graph", __name__)


@blue_index.route("/graph")
def graph():
    return render_template('test/test.html')

@blue_index.route('/live_resource', methods=['GET'])
def live_resource():
    cpu = psutil.cpu_percent()
    date = [time()*1000, cpu]
    response = make_response(json.dumps(date))
    response.content_type = 'application/json'
    return response

@blue_index.route('/graph/live_gas', methods=['GET'])
def live_gas():
    gas_sql = " SELECT payload,TIME(real_t) FROM GAS ORDER BY id DESC LIMIT 1"
    
    gas_db = dbModule.Database()
    gas_row = gas_db.executeAll(gas_sql)
    
    gas_data = make_response(json.dumps(gas_row, default=str))
    gas_data.content_type= 'application/json'  
    return gas_data





    
