from flask import Flask, render_template, json, request
import os

app = Flask(__name__)

#@app.route("/")
#def hello():
#	return render_template("index1.html")

@app.route("/")
def web():
	return render_template('indexR.html')

@app.route('/index')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(port = 5000)
