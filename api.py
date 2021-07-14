import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    ip='192.68.0.44'
    username='mleontenko'
    password='marin123'

    return ip + ' ' + username + ' ' + password

app.run()