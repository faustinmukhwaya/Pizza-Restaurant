from flask import Blueprint, jsonify, request
from ..models.restaurant import Restaurant
from ..models.restaurant_pizza import RestaurantPizza
from ..app import db

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([
        {'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants
    ])

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [
            {
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            } for rp in restaurant.restaurant_pizzas
        ]
    })

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
