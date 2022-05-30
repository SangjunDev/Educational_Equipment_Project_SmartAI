from flask import Blueprint, render_template 
import pymysql 
import numpy as np

blue_read = Blueprint("read_db", __name__)

def db_connector():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234qwer', db='SmartAI', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT * FROM SmartAI.Test;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)
 

@blue_read.route('/test')
def index():
    a = db_connector()
    return a