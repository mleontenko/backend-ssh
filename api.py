import flask
from flask import request
import paramiko
import pprint
import subprocess
from flask import json
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
@cross_origin()
def home():
    request_data = request.get_json()

    host = request_data["ip"]
    username = request_data["username"]
    password = request_data["password"]
    port = 22

    command = "ps aux "

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()

    headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
    raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
    data = [dict(zip(headers, r)) for r in raw_data]

    #print(data)

    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )

    return response

app.run()