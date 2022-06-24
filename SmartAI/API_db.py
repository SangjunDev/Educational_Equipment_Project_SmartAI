from flask import Blueprint, make_response, redirect, url_for
import json
import sys


from SmartAI.module import dbModule


blue_api = Blueprint("api_db", __name__)

sql = { 'illuminace' : 'SELECT id,topic,payload,time(real_t) FROM ILLUMINANCE ORDER BY id DESC LIMIT 1',
        'gas': 'SELECT id,topic,payload,time(real_t) FROM GAS ORDER BY id DESC LIMIT 1',
        'temp': 'SELECT id,topic,payload_t,payload_h,time(real_t) FROM TEMP ORDER BY id DESC LIMIT 1',
        'dust': 'SELECT id,topic,payload,time(real_t) FROM DUST ORDER BY id DESC LIMIT 1',
        'pir': 'SELECT id,topic,payload,time(real_t) FROM PIR ORDER BY id DESC LIMIT 1'
}


def exportJson(query, args={}):
    db=dbModule.Database()
    row = db.executeAll(query, args={})
    data = make_response(json.dumps(row, default=str))
    data.content_type = 'application/json'
    return data


@blue_api.route('/json/illumunance', methods=['GET'])
def live_illumunance():
    try:
        return exportJson(sql['illuminace'])
    except dbModule.Error as e:
        return redirect(url_for('/'))

@blue_api.route('/json/gas', methods=['GET'])
def live_gas():
    try:
        return  exportJson(sql['gas'])
    except dbModule.Error as e:
        return redirect(url_for('/'))

@blue_api.route('/json/temp', methods=['GET'])
def live_temp():
    try:
        return exportJson(sql['temp'])
    except dbModule.Error as e:
        return redirect(url_for('/'))
        
@blue_api.route('/json/pir', methods=['GET'])
def live_pir():
    try:
        return exportJson(sql['pir'])
    except dbModule.Error as e:
        return redirect(url_for('/'))
        
@blue_api.route('/json/dust', methods=['GET'])
def live_dust():
    try:
        return exportJson(sql['dust'])
    except dbModule.Error as e:
        return redirect(url_for('/'))

    
    

 



    