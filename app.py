from models import *
from auth import auth_bp
from views import views_bp
from config import Config
from flask import Flask

# API url & key
URL = "http://www.omdbapi.com/?"
api_key = "2265b973"

TMBD_KEY = "f4b52c3670b8f6f64a5b5c1310e0a37e"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNGI1MmMzNjcwYjhmNmY2NGE1YjVjMTMxMGUwYTM3ZSIsInN1YiI6IjY2M2NkZjgyMzMzMjM2ZDg1OWEzYWYwNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.E9n00Hu42cmHNv6796nZ0nqqaiM9Z52dCbV3s-3u5CQ"

# create a Flask instance
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(views_bp)

if __name__ == "__main__":
    # only run when initially setting up tables for the db
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(debug=True)