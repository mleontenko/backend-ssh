import flask
from flask import request
import paramiko

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def home():
    host = request.form["ip"]
    username = request.form["username"]
    password = request.form["password"]
    port = 22

    command = "ls"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    lines=str(lines)
    #print(lines)
    
    return lines

app.run()