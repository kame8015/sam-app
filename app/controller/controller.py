from flask import Blueprint, request, jsonify
import json

from usecase.usecase import UseCase

controller_api = Blueprint('controller_api', __name__)

usecase = UseCase()

@controller_api.route('/')
def hello_world():
    return usecase.hello_world()

@controller_api.route('/products', methods=['GET'])
def list():
    try:
        products = usecase.get_list()
        return products, 200
    except:
        return "System error.", 500
