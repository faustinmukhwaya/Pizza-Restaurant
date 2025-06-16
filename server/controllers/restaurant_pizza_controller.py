from flask import Blueprint, request, jsonify
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..app import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    errors = []
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate presence
    if price is None:
        errors.append('Price is required')
    if pizza_id is None:
        errors.append('pizza_id is required')
    if restaurant_id is None:
        errors.append('restaurant_id is required')

    # Validate types
    try:
        price = int(price)
    except (TypeError, ValueError):
        errors.append('Price must be an integer')
    try:
        pizza_id = int(pizza_id)
    except (TypeError, ValueError):
        errors.append('pizza_id must be an integer')
    try:
        restaurant_id = int(restaurant_id)
    except (TypeError, ValueError):
        errors.append('restaurant_id must be an integer')

    # Validate price range
    if not errors and not RestaurantPizza.validate_price(price):
        errors.append('Price must be between 1 and 30')

    # Validate existence
    pizza = Pizza.query.get(pizza_id) if not errors else None
    restaurant = Restaurant.query.get(restaurant_id) if not errors else None
    if not errors and (not pizza or not restaurant):
        errors.append('Invalid pizza_id or restaurant_id')

    if errors:
        return jsonify({'errors': errors}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza_id,
        'restaurant_id': rp.restaurant_id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201
