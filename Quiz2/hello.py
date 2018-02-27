from flask import Flask, jsonify, json
from flask import request


app = Flask(__name__)
username = []
userid = 0


@app.route('/', methods=['GET'])
def index():
    return "Hello World!"


@app.route('/users', methods=['GET'])
def hello_user():
    return "Welcome to 'users' page! Current users are: name: {} id: {}".format(username, userid)


@app.route('/users/<string:name>', methods=['GET'])
def display_name(name):
    return jsonify({'name': name})


@app.route('/users', methods=['POST'])
def post_users():
    global userid
    name = request.form['name']
    userid += 1
    username.append(name)
    return jsonify({'name': username}, {'id': userid})


@app.route('/users', methods=['DELETE'])
def del_users():
    name = request.form['name']
    username.remove(name)
    return "Requested user deleted."
