from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config import Config
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp



migrate=Migrate()

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(pizza_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')

    return app

# if __name__ =='__main__':
#      app.run(debug= True, port = 4000)
#     # with app.app_context():
#     #     db.create_all()
#     #     app.run(debug =True)