
from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

# Example seed data
restaurants = [
    Restaurant(name="Luigi's", address="123 Main St"),
    Restaurant(name="Kiki's Pizza", address="456 Side Ave"),
]
pizzas = [
    Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese"),
    Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
]

def seed():
    db.drop_all()
    db.create_all()
    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.commit()
    # Add join table entries
    rp1 = RestaurantPizza(price=10, restaurant_id=restaurants[0].id, pizza_id=pizzas[0].id)
    rp2 = RestaurantPizza(price=12, restaurant_id=restaurants[1].id, pizza_id=pizzas[1].id)
    db.session.add_all([rp1, rp2])
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed()
        print("Seeded database!")
