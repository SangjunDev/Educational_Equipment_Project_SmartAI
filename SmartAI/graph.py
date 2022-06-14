from flask import Blueprint, Response, make_response, render_template
from time import time
import json
import psutil


blue_dbAPI = Blueprint("graph", __name__)


@blue_dbAPI.route("/graph")
def graph():
    return render_template('test/test.html')

@blue_dbAPI.route('/live_resource', methods=['GET'])
def live_resource():
    cpu = psutil.cpu_percent()
    date = [time()*1000, cpu]
    response = make_response(json.dumps(date))
    response.content_type = 'application/json'
    return response







    
