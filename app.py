from models import *
from auth import auth_bp
from views import views_bp
from config import Config
from flask import Flask
from extensions import bcrypt

# create a Flask instance
app = Flask(__name__)
app.config.from_object(Config)
bcrypt.init_app(app)
db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(views_bp)

if __name__ == "__main__":
    # only run when initially setting up tables for the db
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)
