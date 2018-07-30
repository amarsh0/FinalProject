from flask import Flask, request, render_template
import subprocess
import json

app = Flask(__name__)

with open('static/test.json') as data_file:
    data_load = json.load(data_file)

columns = [
    {
        "field": "player_name",
        "title": "Name",
        "sortable": True,
    },
    {
        "field": "receiving_tds",
        "title": "Touchdowns",
        "sortable": True,
    },
    {
        "field": "passing_yds",
        "title": "Passing Yards",
        "sortable": True,
    },
]

@app.route("/")
def index():
    return render_template('index.html', data=data_load, columns=columns, title='is this part needed?')

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