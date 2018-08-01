from flask import Flask, request, render_template
import subprocess
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/echo", methods=['POST'])
def echo():
    command = request.form['text']
    subprocess.call([command])
    #return request.form['text'] + " Command executed via subprocess"
    return index()

@app.route('/', methods=['POST'])
def getStatus():
    teamNum = request.form['teamNum']
    return teamNum

if __name__ == "__main__":
    app.run(debug='True')
