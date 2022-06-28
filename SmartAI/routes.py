from flask import Blueprint, render_template 
from SmartAI.module import dbModule as db

blue_index = Blueprint("index", __name__)

'''Main Page Mapping'''
@blue_index.route("/")
def main():
 return render_template('actuator_section/actuator.html')

'''Voice Page Mapping'''
@blue_index.route("/voice")
def voice_recognition():
    return render_template('/voice_recognition.html')

'''Actuator Page Mapping'''
@blue_index.route("/Actuator")
def actuator_control():
    return render_template('actuator_section/actuator.html')

'''Sensor Page Mapping'''
@blue_index.route("/Sensor/Illuminance")                                            
def sensor_illumunance():
    return render_template('sensor_section/Illuminance.html', 
                           datas= db.raedData(db.allSelect['illuminace']))

@blue_index.route("/Sensor/Gas")
def sensor_gas():
    return render_template('sensor_section/Gas.html', 
                           datas= db.raedData(db.allSelect['gas']))

@blue_index.route("/Sensor/Temp")
def sensor_temp():
    return render_template('sensor_section/Temp.html', 
                           datas= db.raedData(db.allSelect['temp']) )    

@blue_index.route("/Sensor/Dust")
def sensor_dust():

    return render_template('sensor_section/Dust.html',  
                           datas= db.raedData(db.allSelect['dust']))

@blue_index.route("/Sensor/Pir")
def sensor_pir():

    return render_template('sensor_section/Pir.html',  
                           datas= db.raedData(db.allSelect['pir'])  )

'''Module Page Mapping'''
@blue_index.route("/Module/Light")
def module_light():
    return render_template('module_section/Light.html',  
                           datas= db.raedData(db.allSelect['illuminace']))

@blue_index.route("/Module/Gas")
def module_gas():
    return render_template('module_section/Gas.html',  
                           datas= db.raedData(db.allSelect['gas']))

@blue_index.route("/Module/Temp")
def module_temp():
    return render_template('/module_section/Temp.html',  
                           datas= db.raedData(db.allSelect['temp']))

@blue_index.route("/Module/Dust")
def module_dust():
    return render_template('module_section/Dust.html',  
                           datas= db.raedData(db.allSelect['dust']))

@blue_index.route("/Module/Pir")
def module_pir():
    return render_template('module_section/Pir.html',  
                           datas= db.raedData(db.allSelect['pir']))


