import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def home():
    ip = request.form["ip"]
    username = request.form["username"]
    password = request.form["password"]
    
    return ip

app.run()