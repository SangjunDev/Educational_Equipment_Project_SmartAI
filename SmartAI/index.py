from flask import Blueprint, render_template 

blue_index = Blueprint("index", __name__)

@blue_index.route("/")
def main():
 return render_template('index.html')

@blue_index.route("/test")
def main2():
 return render_template('test.html')

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
    return render_template('sensor_section/Illuminance.html')

@blue_index.route("/Sensor/Gas")
def sensor_gas():
    return render_template('sensor_section/Gas.html')

@blue_index.route("/Sensor/Temp")
def sensor_temp():
    return render_template('sensor_section/Temp.html')

@blue_index.route("/Sensor/Dust")
def sensor_dust():
    return render_template('sensor_section/Dust.html')

@blue_index.route("/Sensor/Pir")
def sensor_pir():
    return render_template('sensor_section/Pir.html')

'''Module Page Mapping'''
@blue_index.route("/Module/Light")
def module_light():
    return render_template('module_section/Light.html')

@blue_index.route("/Module/Gas")
def module_gas():
    return render_template('module_section/Gas.html')

@blue_index.route("/Module/Temp")
def module_temp():
    return render_template('module_section/Temp.html')

@blue_index.route("/Module/Dust")
def module_dust():
    return render_template('module_section/Dust.html')

@blue_index.route("/Module/Pir")
def module_pir():
    return render_template('module_section/Pir.html')


