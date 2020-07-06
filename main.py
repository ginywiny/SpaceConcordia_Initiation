from flask import Flask, redirect, url_for, render_template, request, jsonify
from arduinoWrite import *
import arduinoWrite
import serial
import time

arduinoObj = Arduino()
app = Flask(__name__)

# #Display the entire GUI, and cause LED to turn on, off, blink, not blink, display temperature and change blink speed
@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == "POST": 
        if request.form['submit'] == 'Turn On':
            print("TURN ON FROM MAIN")
            arduinoObj.setLight()

        elif request.form['submit'] == 'Turn Off':
            print("TURN OFF FROM MAIN")
            arduinoObj.setLightOff()

        elif request.form['submit'] == "Blink On":
            print("BLINK ON FROM MAIN")
            arduinoObj.setBlink(breakBit=0)
            # if request.form['submit'] == "Turn Off":
            #     arduinoObj.setBlink(breakBit=1)

        else: 
            pass
    return render_template("dy1.html")

@app.route('/about')
def aboutPage():
    return render_template("about.html")

@app.route('/_stuff', methods = ['GET'])
def stuff():
    return jsonify(result = arduinoWrite.getData())

if __name__ == "__main__":
    app.run(debug=True)
