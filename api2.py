from flask import Flask, request
from flask import json
from flask_restful import Resource, Api
import paramiko

app = Flask(__name__)
api = Api(app)

class GetData(Resource):
    def post(self):
        some_json = request.get_json()
        
        return {'you sent': some_json}, 201

api.add_resource(GetData, '/')

if __name__ == '__main__':
    app.run(debug=True)