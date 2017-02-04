from flask import Flask
from flask import render_template
import requests
import datetime


app = Flask(__name__)
PGE_URL = "http://localhost:8000/api/push/test_app/"

@app.route('/')
@app.route('/<name>')
def hello_world(name="Anonymous"):
    return render_template('index.html', name=name)

@app.route('/push/<name>/')
def push(name):
    j = {"name":name, "datetime":datetime.datetime.now().isoformat()}
    print(j)
    requests.post(PGE_URL, data = j)
    return hello_world(name)
