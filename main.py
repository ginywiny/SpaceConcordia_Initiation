from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from arduinoWrite import *
import arduinoWrite
import serial
import time

arduinoObj = Arduino()
app = Flask(__name__)
app.secret_key = "SEKRETKEY_WOW"

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
            
            if (blinkSpeedString.isdigit()):
                blinkSpeedFloat = float(blinkSpeedString)
                flash("Valid blink duration set to %s" % blinkSpeedString)
            
            else:
                flash("Invalid blink duration \"%s\", default duration set to 1" % blinkSpeedString)
                blinkSpeedFloat = 1
            
            print("Blinkspeed is: %s" % blinkSpeedString)

            if (blinkSpeedFloat <= 5 and blinkSpeedFloat > 0 and len(blinkSpeedString) <= 2 and len(blinkSpeedString) >= 0 and blinkSpeedString.isdigit()):
                print("Blinkspeed VALID: %s" % blinkSpeedString)
                arduinoObj.setBlinkSpeed(blinkSpeedFloat)
                arduinoObj.setBlink(blink=blinkSpeedFloat)
                return redirect(request.url)
            else:
                print("Blinkspeed INVALID: %s" % blinkSpeedString)
                arduinoObj.setBlinkSpeed(blink=1)
                arduinoObj.setBlink(blink=1)
                return redirect(request.url)

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