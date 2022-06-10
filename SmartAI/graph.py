from urllib import response
from flask import Blueprint, make_response, render_template
from time import time
import json
import psutil

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



    
