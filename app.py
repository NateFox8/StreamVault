from models import *
from auth import auth_bp
from config import Config
from flask import Flask, render_template, redirect, url_for, request, session, current_app
from functools import wraps
import requests

# API url & key
URL = "http://www.omdbapi.com/?"
api_key = "2265b973"

# create a Flask instance
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(auth_bp)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET'])
@login_required
def index():        
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
@login_required
def home():        
    return render_template('home.html')

@app.route('/watch_list', methods=['GET'])
@login_required
def watch_list():        
    return render_template('watch_list.html')

@app.route('/favorites', methods=['GET'])
@login_required
def favorites():        
    return render_template('favorites.html')

@app.route('/profile', methods=['GET'])
@login_required
def profile():        
    return render_template('profile.html')

@app.route('/search', methods=['GET'])
@login_required
def search():        
    title = request.args.get('title')    
    
    if title:
        PARAMS = {'apikey': api_key, 't': title, 'plot': 'full'}
        response = requests.get(url=URL, params=PARAMS)
        movie_data = response.json()
        return render_template('search.html', movie_data=movie_data)
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    # only run when initially setting up tables for the db
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(debug=True)