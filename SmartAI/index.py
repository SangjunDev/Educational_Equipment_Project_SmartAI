from flask import Blueprint, render_template 

from SmartAI.module import dbModule

blue_index = Blueprint("index", __name__)

sql = { 'illuminace' : 'SELECT * FROM ILLUMINANCE',
        'gas': 'SELECT * FROM GAS',
        'temp': 'SELECT * FROM TEMP',
        'dust': 'SELECT * FROM DUST',
        'pir': 'SELECT * FROM PIR'
}

@blue_index.route("/")
def main():
 return render_template('index.html')

@blue_index.route("/test2")
def test():
 return render_template('test/test.html')

'''Actuator Page Mapping'''
@blue_index.route("/Actuator")
def actuator_control():
    return render_template('actuator_section/actuator.html')


'''Sensor Page Mapping'''
@blue_index.route("/Sensor/Illuminance")                                            
def sensor_illumunance():
    db = dbModule.Database()
    data = db.raedTable(sql['illuminace'])
    return render_template('sensor_section/Illuminance.html', datas= data)

@blue_index.route("/Sensor/Gas")
def sensor_gas():
    db = dbModule.Database()
    data = db.raedTable(sql['gas'])
    return render_template('sensor_section/Gas.html', datas= data)

@blue_index.route("/Sensor/Temp")
def sensor_temp():
    db = dbModule.Database()
    data = db.raedTable(sql['temp']) 
    return render_template('sensor_section/Temp.html', datas= data)    

@blue_index.route("/Sensor/Dust")
def sensor_dust():
    db = dbModule.Database()
    data = db.raedTable(sql['dust'])
    return render_template('sensor_section/Dust.html',  datas= data)

@blue_index.route("/Sensor/Pir")
def sensor_pir():
    db = dbModule.Database()
    data = db.raedTable(sql['pir'])    
    return render_template('sensor_section/Pir.html',  datas= data)

'''Module Page Mapping'''
@blue_index.route("/Module/Light")
def module_light():
    db = dbModule.Database()
    data = db.raedTable(sql['illuminace'])
    return render_template('module_section/Light.html',  datas= data)

@blue_index.route("/Module/Gas")
def module_gas():
    db = dbModule.Database()
    data = db.raedTable(sql['gas'])
    return render_template('module_section/Gas.html',  datas= data)

@blue_index.route("/Module/Temp")
def module_temp():
    db = dbModule.Database()
    data = db.raedTable(sql['temp'])
    return render_template('module_section/Temp.html',  datas= data)

@blue_index.route("/Module/Dust")
def module_dust():
    db = dbModule.Database()
    data = db.raedTable(sql['dust'])
    return render_template('module_section/Dust.html',  datas= data)

@blue_index.route("/Module/Pir")
def module_pir():
    db = dbModule.Database()
    data = db.raedTable(sql['pir'])
    return render_template('module_section/Pir.html',  datas= data)


