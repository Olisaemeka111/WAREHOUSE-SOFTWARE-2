from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import items, orders

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(items.bp)
app.register_blueprint(orders.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
