from flask import Flask, jsonify
import awsgi

app = Flask('sam-chalice')
app.config['JSON_AS_ASCII'] = False

@app.route('/hello')
def index():
    return jsonify({'hello': 'world'})

@app.route('/hello/<name>')
def hello_name(name):
    return jsonify({'hello': name})

def lambda_handler(event, context):
    return awsgi.response(app, event, context)
