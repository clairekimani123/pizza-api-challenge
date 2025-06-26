from flask import Blueprint, jsonify
from server.models import Restaurant, db

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/', methods=['GET'])

def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [
        {   "id": r.id,
            "name": r.name,
            "address": r.address
        } for r in restaurants
    ]
    return jsonify(result), 200

@restaurant_bp.route('/<int:id>', methods=['GET'])

def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    result = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [
            {
                "id": restopizz.pizza.id,
                "name": restopizz.pizza.name,
                "ingredients": restopizz.pizza.ingredients
            } for restopizz in restaurant.restaurant_pizzas
        ]
    }
    return jsonify(result), 200

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204