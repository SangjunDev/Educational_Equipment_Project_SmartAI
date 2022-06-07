from flask import Blueprint, render_template 

blue_index = Blueprint("index", __name__)

@blue_index.route("/")
def main():
 return render_template('index.html')

@blue_index.route("/Light_Section")
def Light_Section():
    return render_template('Light_Module.html')

@blue_index.route("/Gas_Section")
def Gas_Section():
    return render_template('Gas.html')

@blue_index.route("/Temp_Section")
def Temp_Section():
    return render_template('Temp.html')

@blue_index.route("/Dust_Section")
def Dust_Section():
    return render_template('Dust.html')

@blue_index.route("/Pir_Section")
def Pir_Section():
    return render_template('Pir.html')

@blue_index.route("/button")
def button():
    return render_template('components/buttons.html')

@blue_index.route("/2")
def main2():
 return render_template('test/index.html')
