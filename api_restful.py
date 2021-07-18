from flask import Flask, request
from flask import json
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import paramiko

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

class GetData(Resource):
    def post(self):
        request_data = request.get_json()

        host = request_data["ip"]
        username = request_data["username"]
        password = request_data["password"]
        port = 22

        command = "ps aux"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.readlines()

        # parse output
        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        data = [dict(zip(headers, r)) for r in raw_data]

        return data

api.add_resource(GetData, '/')

if __name__ == '__main__':
    app.run(debug=True)