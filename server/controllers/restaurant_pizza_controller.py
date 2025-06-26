from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Pizza, Restaurant, db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/', methods=['POST'])
def make_restaurant_pizza():
    data = request.get_json()

    price = data.get("price")
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    new_resPrice = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )

    db.session.add(new_resPrice)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    result = {
        "id": new_resPrice.id,
        "price": new_resPrice.price,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }

    return jsonify(result), 201