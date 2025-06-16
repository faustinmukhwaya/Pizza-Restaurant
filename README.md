# Pizza Restaurant API

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell
   ```

2. **Set up the database:**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

3. **Seed the database:**
   ```bash
   python server/seed.py
   ```

---

## Project Structure (MVC)

```
server/
    app.py                # App setup
    config.py             # DB config
    models/               # SQLAlchemy models
    controllers/          # Route handlers
    seed.py               # Seed data
migrations/               # DB migrations
```

---

## Routes

### GET /restaurants
Returns a list of all restaurants.

### GET /restaurants/<id>
Returns details of a single restaurant and its pizzas.
- If not found: `{ "error": "Restaurant not found" }` (404)

### DELETE /restaurants/<id>
Deletes a restaurant and all related RestaurantPizzas.
- If successful: 204 No Content
- If not found: `{ "error": "Restaurant not found" }` (404)

### GET /pizzas
Returns a list of pizzas.

### POST /restaurant_pizzas
Creates a new RestaurantPizza.
- **Request:**
  ```json
  { "price": 5, "pizza_id": 1, "restaurant_id": 3 }
  ```
- **Success response:**
  ```json
  { "id": 4, "price": 5, "pizza_id": 1, "restaurant_id": 3, "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" }, "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "address3" } }
  ```
- **Error response:**
  ```json
  { "errors": ["Price must be between 1 and 30"] }
  ```
  (400 Bad Request)

---

## Validation Rules
- `RestaurantPizza.price` must be between 1 and 30 (inclusive).

---

## Postman Usage
- Import `challenge-1-pizzas.postman_collection.json` into Postman.
- Test each route as described above.

---

## Submission Checklist
- [x] MVC folder structure
- [x] Models with validations and relationships
- [x] All routes implemented
- [x] Postman tests passing
- [x] Well-written README.md
