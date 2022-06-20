from flask import Blueprint, make_response, request
import json


from SmartAI.module import dbModule

blue_api = Blueprint("api_db", __name__)

sql = { 'illuminace' : 'SELECT id,topic,payload,time(real_t) FROM ILLUMINANCE ORDER BY id DESC LIMIT 1',
        'gas': 'SELECT id,topic,payload,time(real_t) FROM GAS ORDER BY id DESC LIMIT 1',
        'temp': 'SELECT id,topic,payload_t,payload_h,time(real_t) FROM TEMP ORDER BY id DESC LIMIT 1',
        'dust': 'SELECT id,topic,payload,time(real_t) FROM DUST ORDER BY id DESC LIMIT 1',
        'pir': 'SELECT id,topic,payload,time(real_t) FROM PIR ORDER BY id DESC LIMIT 1'
}


@blue_api.route('/json/illumunance', methods=['GET'])
def live_illumunance():
    db=dbModule.Database()
    row = db.executeAll(sql['illuminace'])
    ill_data = make_response(json.dumps(row, default=str))
    ill_data.content_type= 'application/json'
    
    return ill_data

@blue_api.route('/json/gas', methods=['GET'])
def live_gas():
    db=dbModule.Database()
    row = db.executeAll(sql['gas'])
    gas_data = make_response(json.dumps(row, default=str))
    gas_data.content_type= 'application/json'
    
    return gas_data

@blue_api.route('/json/temp', methods=['GET'])
def live_temp():
    db=dbModule.Database()
    row = db.executeAll(sql['temp'])
    temp_data = make_response(json.dumps(row, default=str))
    temp_data.content_type= 'application/json'
    
    return temp_data

@blue_api.route('/json/pir', methods=['GET'])
def live_pir():
    db=dbModule.Database()
    row = db.executeAll(sql['pir'])
    pir_data = make_response(json.dumps(row, default=str))
    pir_data.content_type= 'application/json'
    return pir_data

@blue_api.route('/json/dust', methods=['GET'])
def live_dust():
    db=dbModule.Database()
    row = db.executeAll(sql['dust'])
    dust_data = make_response(json.dumps(row, default=str))
    dust_data.content_type= 'application/json'
    
    return dust_data


    
    

 



    