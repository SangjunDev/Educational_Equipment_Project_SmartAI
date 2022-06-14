from flask import Blueprint, render_template 

from SmartAI.module import dbModule

blue_index = Blueprint("index", __name__)

@blue_index.route("/")
def main():
 return render_template('index.html')

@blue_index.route("/test")
def main2():
 return render_template('test/test.html')

'''Actuator Page Mapping'''
@blue_index.route("/Actuator/LED")
def actuator_light():
    return render_template('actuator_section/LED.html')

@blue_index.route("/Actuator/Fan")
def actuator_gas():
    return render_template('actuator_section/Fan.html')

@blue_index.route("/Actuator/SolenoidValve")
def actuator_solenoidvalve():
    return render_template('actuator_section/SolenoidValve.html')

@blue_index.route("/Actuator/DoorLock")
def actuator_doorlock():
    return render_template('actuator_section/DoorLock.html')

@blue_index.route("/Actuator/Switch")
def actuator_switch():
    return render_template('actuator_section/Switch.html')


'''Sensor Page Mapping'''
@blue_index.route("/Sensor/Illuminance")
def sensor_illumunance():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM ILLUMINANCE"
    
    row = table_db.executeAll(sql)
    return render_template('sensor_section/Illuminance.html', rows=row)

@blue_index.route("/Sensor/Gas")
def sensor_gas():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM GAS"
    
    row = table_db.executeAll(sql)
    return render_template('sensor_section/Gas.html', rows=row)

@blue_index.route("/Sensor/Temp")
def sensor_temp():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM TEMP"
    row = table_db.executeAll(sql)    
    return render_template('sensor_section/Temp.html', rows = row)    


@blue_index.route("/Sensor/Dust")
def sensor_dust():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM DUST"
    
    row = table_db.executeAll(sql)
    return render_template('sensor_section/Dust.html', rows=row)

@blue_index.route("/Sensor/Pir")
def sensor_pir():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM ILLUMINANCE"
    
    row = table_db.executeAll(sql)
    return render_template('sensor_section/Pir.html', rows=row)

'''Module Page Mapping'''
@blue_index.route("/Module/Light")
def module_light():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM ILLUMINANCE"
    
    row = table_db.executeAll(sql)
    
    return render_template('module_section/Light.html', rows = row)

@blue_index.route("/Module/Gas")
def module_gas():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM GAS"
    row = table_db.executeAll(sql)

    return render_template('module_section/Gas.html', rows = row)

@blue_index.route("/Module/Temp")
def module_temp():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM TEMP"
    row = table_db.executeAll(sql)    
    return render_template('module_section/Temp.html', rows = row)

@blue_index.route("/Module/Dust")
def module_dust():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM DUST"
    row = table_db.executeAll(sql)    
    return render_template('module_section/Dust.html', rows = row)

@blue_index.route("/Module/Pir")
def module_pir():
    table_db = dbModule.Database()
    
    sql = "SELECT * FROM PIR"
    row = table_db.executeAll(sql)    
    return render_template('module_section/Pir.html', rows = row)


