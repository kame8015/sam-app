# from domain.repository.repository import ProductRepository
from flask import jsonify


products = [
    {
        "name": "coffee",
        "price": 100,
        "stock": 10
    },
    {
        "name": "water",
        "price": 80,
        "stock": 20
    },
    {
        "name": "cola",
        "price": 120,
        "stock": 12
    },
    {
        "name": "monster",
        "price": 180,
        "stock": 50
    }
]

class UseCase:
    # def __init__(self):
    #     self.repository = repository()

    def hello_world(self):
        return "Hello, World!", 200

    def get_list(self) -> dict:
        return jsonify(products)
