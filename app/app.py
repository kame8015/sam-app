from flask import Flask, jsonify
import awsgi
from controller.controller import controller_api

app = Flask('sam-chalice')
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(controller_api)

@app.errorhandler(404)
def error_handler_404(error):
    return jsonify({"error_code": "not_found"}), error.code

@app.errorhandler(405)
def error_handler_405(error):
    return jsonify({"error_code": "method_not_allowed"}), error.code

@app.errorhandler(415)
def error_handler_415(error):
    return jsonify({"error_code": "unsupported_media_type"}), error.code

def lambda_handler(event, context):

    response = awsgi.response(app, event, context)

    return response
