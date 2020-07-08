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

        # if request.form['submit'] == "Start Temperature":
        if request.form.get('submitTemp') == "Start Temperature":
            print("START TIME FROM MAIN")
            if (arduinoObj.getState() == 1):
                arduinoObj.setLight()
            else :
                arduinoObj.setLightOff()

        # if request.form.get('submitOn') == 'Turn On':
        if request.form.get('submitOn'):
            print("TURN ON FROM MAIN")
            arduinoObj.setState(1)
            arduinoObj.setLight()

        # if request.form['submit'] == 'Turn Off':
        if request.form.get('submitOff'):
            print("TURN OFF FROM MAIN")
            arduinoObj.setState(0)
            arduinoObj.setLightOff()

        # elif request.form['submit'] == "Blink On":
        elif request.form.get('submitBlink'):
            arduinoObj.setBlink(1)  
            print("BLINK ON FROM MAIN")

        

        #  if (request.form["submit"] == 'submitBlink'):
        if (not request.form.get("submitSpeed") is None):
            if (arduinoObj.getState() == 1):
                arduinoObj.setLight()
            else :
                arduinoObj.setLightOff() 

            blinkSpeedString = request.form.get("submitSpeed")    #Default value is 1 if nothing entered
            blinkSpeedFloat = float(blinkSpeedString)
            print("Blinkspeed is: %s" % blinkSpeedString)

            #blinkSpeed = (request.form.get("submitBlink", False))    #Default value is 1 if nothing entered
            if (blinkSpeedFloat <= 5 and blinkSpeedFloat > 0 and len(blinkSpeedString) <= 2 and len(blinkSpeedString) >= 0 and blinkSpeedString.isdigit()):
                print("Blinkspeed VALID: %s" % blinkSpeedString)
                arduinoObj.setBlinkSpeed(blinkSpeedFloat)
                arduinoObj.setBlink(blink=blinkSpeedFloat)
            else:
                arduinoObj.setBlinkSpeed(blink=1)
                print("Blinkspeed INVALID: %s" % blinkSpeedString)
                arduinoObj.setBlink(blink=1)

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