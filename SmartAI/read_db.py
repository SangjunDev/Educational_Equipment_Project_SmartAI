from flask import Blueprint, make_response, request
import json

from SmartAI.Module import dbModule

blue_read = Blueprint("read_db", __name__)


@blue_read.route('/sensor/live_illumunance')
def live_illumunance():
    ill_sql = " SELECT payload FROM ILLUMINANCE ORDER BY id DESC LIMIT 1"
    
    ill_db = dbModule.Database()
    
    ill_row = ill_db.executeAll(ill_sql)
    ill_data = make_response(json.dumps(ill_row, default=str))
    ill_data.content_type= 'application/json'
    
    return ill_data

@blue_read.route('/sensor/live_gas')
def live_gas():
    gas_sql = " SELECT payload FROM GAS ORDER BY id DESC LIMIT 1"
    
    gas_db = dbModule.Database()
    gas_row = gas_db.executeAll(gas_sql)
    gas_data = make_response(json.dumps(gas_row, default=str))
    gas_data.content_type= 'application/json'
    
    return gas_data

@blue_read.route('/sensor/live_temp')
def live_temp():

    temp_sql = " SELECT payload_t,payload_h FROM TEMP ORDER BY id DESC LIMIT 1"    
    
    temp_db = dbModule.Database()
    temp_row = temp_db.executeAll(temp_sql)
    temp_data = make_response(json.dumps(temp_row, default=str))
    temp_data.content_type= 'application/json'
    return temp_data

@blue_read.route('/sensor/live_pir')
def live_pir():
    pir_db = dbModule.Database()
    
    pir_sql = " SELECT payload FROM PIR ORDER BY id DESC LIMIT 1"
    pir_row = pir_db.executeAll(pir_sql)
    pir_data = make_response(json.dumps(pir_row, default=str))
    return pir_data

@blue_read.route('/sensor/live_dust')
def live_dust():
    
    dust_sql = " SELECT payload FROM DUST ORDER BY id DESC LIMIT 1"
    
    dust_db = dbModule.Database()
    dust_row = dust_db.executeAll(dust_sql)
    dust_data = make_response(json.dumps(dust_row, default=str))
    dust_data.content_type= 'application/json'
    return dust_data

 



    