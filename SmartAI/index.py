from flask import Blueprint, render_template 

from SmartAI.module import dbModule

blue_index = Blueprint("index", __name__)

def raedTable(query):
    table_db = dbModule.Database()
    row = table_db.executeAll(query)
    return row

@blue_index.route("/")
def main():
 return render_template('index.html')

'''Actuator Page Mapping'''
@blue_index.route("/Actuator")
def actuator_control():
    return render_template('actuator_section/actuator.html')



'''Sensor Page Mapping'''
@blue_index.route("/Sensor/Illuminance")
def sensor_illumunance():
    sql = "SELECT * FROM ILLUMINANCE"
    
    return render_template('sensor_section/Illuminance.html', rows=raedTable(sql))

@blue_index.route("/Sensor/Gas")
def sensor_gas():
    sql = "SELECT * FROM GAS"

    return render_template('sensor_section/Gas.html', rows=raedTable(sql))

@blue_index.route("/Sensor/Temp")
def sensor_temp():
    sql = "SELECT * FROM TEMP" 
    
    return render_template('sensor_section/Temp.html', rows = raedTable(sql))    


@blue_index.route("/Sensor/Dust")
def sensor_dust():
    sql = "SELECT * FROM DUST"


    return render_template('sensor_section/Dust.html', rows=raedTable(sql))

@blue_index.route("/Sensor/Pir")
def sensor_pir():
    sql = "SELECT * FROM ILLUMINANCE"
    

    return render_template('sensor_section/Pir.html', rows=raedTable(sql))

'''Module Page Mapping'''
@blue_index.route("/Module/Light")
def module_light():
    sql = "SELECT * FROM ILLUMINANCE"

    return render_template('module_section/Light.html', rows = raedTable(sql))

@blue_index.route("/Module/Gas")
def module_gas():
    sql = "SELECT * FROM GAS"

    return render_template('module_section/Gas.html', rows = raedTable(sql))

@blue_index.route("/Module/Temp")
def module_temp():
    sql = "SELECT * FROM TEMP"  
    return render_template('module_section/Temp.html', rows =raedTable(sql))

@blue_index.route("/Module/Dust")
def module_dust():
    sql = "SELECT * FROM DUST"
    
    return render_template('module_section/Dust.html', rows = raedTable(sql))

@blue_index.route("/Module/Pir")
def module_pir():
    sql = "SELECT * FROM PIR"
    
    return render_template('module_section/Pir.html', rows = raedTable(sql))


