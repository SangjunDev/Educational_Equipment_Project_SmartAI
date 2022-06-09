from urllib import response
from flask import Blueprint, jsonify, make_response, render_template, request
import pymysql 
from flask_paginate import Pagination, get_page_args
import json
import datetime

blue_read = Blueprint("read_db", __name__)

db = pymysql.connect(host='localhost', 
                     port=3306, user='root', 
                     passwd='1234qwer', 
                     db='SmartAI', 
                     charset='utf8')

cursor = db.cursor()


@blue_read.route('/sensor/re_gas')
def live_gas():
    sql_1 = " SELECT payload FROM GAS ORDER BY id DESC LIMIT 1"
    cursor.execute(sql_1)
    data = json.dumps(cursor.fetchall())
    
    return data
 



    