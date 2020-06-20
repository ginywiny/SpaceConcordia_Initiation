from flask import Flask, redirect, url_for, render_template, request, jsonify
import arduinoWrite

app = Flask(__name__)

# #Display the entire GUI, and cause LED to turn on, off, blink, not blink, display temperature and change blink speed
# @app.route("/")
# def home():
#     arduinoWrite.setLightOff()
#     #temperature = arduinoWrite.getData()
#     #return render_template("index.html", val1 = temperature)
#     return render_template("index.html")



@app.route("/")
def home():
    return render_template("dy1.html")

@app.route('/_temperature', methods = ['GET'])
def updateTemperature():
    return jsonify(val1 = arduinoWrite.getData())

@app.route('/_stuff', methods = ['GET'])
def stuff():
    return jsonify(result = arduinoWrite.getData())



# Send blink speed to be read
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        blinkSpeed = request.form['blinkSpeed']
        return render_template('index.html', blinkSpeed = blinkSpeed)
    else:
        return render_template('index.html')


#Not necessary, use this for example
@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))    
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    #arduinoWrite.setLight()
    return render_template("gui.html", content = usr)
    #return f"<h1>{usr}</h1>"

@app.route("/gui")
def gui():
    return render_template("gui.html")

#@app.route("/<name>")
#def user(name):
    #arduinoWrite.setLight()        Used to set the arduino light when accessing page
    #return render_template("index.html", content = name, content2 = "Nice", content3 = ["tim", "joe", "bill"])

if __name__ == "__main__":
    app.run(debug=True)
