This is a practice of a RESTFUL API REstaurant  that I build using Flask, Flask=SQLAlchemy and Flask migrate. There is also the use or the support of CRUD operation for restaurant, pizzas, and restaurant-pizza asssociations. And also the use of validations and constraints.

##Setup Instructions##

1: as norm you clone the repository:
git clone  https://github.com/your-username/pizza-api-challenge.git

cd pizza-api-challenge

2: Create and activate the virtual enviroment
pipenv install
pipenv shell
pipenv install flask flask-sqlalchemy flask-migrate

3: Set up Flask application
export FLASK_APP=SERVER/app.py
export FLASK_RUN_PORT=5555

4: Initialize the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5: Seed the dAatabase
python server/seed.py

6: Run Application
flask run


Database Migration and Seeding
The database is a SQLLite database(pizza-restaurant.db)
Then you run th migration to create table.
flask db migrate
flask db upgrade

seed the database with a sample data:
python server/seed.py


##Route Summary##

GET /restaurants

-Returns a list of restaurants with their pizzas.
-Response (200):
    [
    {
        "id": 1,
        "name": "Domino's Pizza",
        "address": "123 Main St",
        "restaurant_pizzas": [...]
    },
    ...
]

GET /restaurants/int:id

-Returns details of a specific restaurant and its pizzas.
-Response(200)
    {
    "id": 1,
    "name": "Domino's Pizza",
    "address": "123 Main St",
    "restaurant_pizzas": [...]
}

Error (404):
{"error": "Restaurant not found"}

DELETE /restaurants/int:id

-Deletes a restaurant and its associated -RestaurantPizzas.
-Response (204):
    -No content
-Error (404):
{"error": "Restaurant not found"}

GET /pizzas

Returns a list of all pizzas.
Response (200):

[
    {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Tomato Sauce, Mozzarella, Basil"
    },
    ...
]

POST/restaurant-pizzas
-create a new RestaurantPizza
-request

{
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3
}


##Validation Rules##
-Restaurant:
    -name: Required, non-empty string (enforced by @validates)
    -address: Required, non-empty string (enforced by @validates)
-Pizza:
    -name: Required, non-empty string (enforced by @validates)
    -ingredients: Required, non-empty string (enforced by @validates)
-RestaurantPizza:
    -price: Required, integer between 1 and 30 (enforced by @validates)
    -restaurant_id, pizza_id: Valid foreign keys (checked in controller)

 ##Postman Usage##
 1: Install Postman
2: Import the collection:
    -Open Postman, click Import, and upload challenge-1-pizzas.postman_collection.json.

3: Test routes:
    -Run each request in the collection to verify API endpoints.

   
   ##ProjectStructure##

   pizza-api-challenge/
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.mdflask db init
flask db migrate -m "Initial migration"
flask db upgrade