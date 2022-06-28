from flask import Blueprint, make_response, redirect, url_for
import json
from SmartAI.module import dbModule as db


blue_api = Blueprint("api_db", __name__)


def exportJson(query, args={}):
    data = make_response(json.dumps
                         (db.raedData(query, args={}), 
                          default=str))
    data.content_type = 'application/json'
    return data


@blue_api.route('/json/illumunance', methods=['GET'])
def live_illumunance():
    try:
        return exportJson(db.apiSql['illuminace'])
    except db.Error as e:
        return redirect(url_for('/'))

@blue_api.route('/json/gas', methods=['GET'])
def live_gas():
    try:
        return  exportJson(db.api_sql['gas'])
    except db.Error as e:
        return redirect(url_for('/'))

@blue_api.route('/json/temp', methods=['GET'])
def live_temp():
    try:
        return exportJson(db.api_sql['temp'])
    except db.Error as e:
        return redirect(url_for('/'))
        
@blue_api.route('/json/pir', methods=['GET'])
def live_pir():
    try:
        return exportJson(db.api_sql['pir'])
    except db.Error as e:
        return redirect(url_for('/'))
        
@blue_api.route('/json/dust', methods=['GET'])
def live_dust():
    try:
        return exportJson(db.api_sql['dust'])
    except db.Error as e:
        return redirect(url_for('/'))

    
    

 



    