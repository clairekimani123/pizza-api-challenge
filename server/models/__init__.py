from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from . pizza import Pizza
from . restaurant import Restaurant
from . restaurant_pizza import RestaurantPizza