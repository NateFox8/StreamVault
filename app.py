from models import *
from auth import auth_bp
from config import Config
from flask import Flask, render_template, redirect, url_for, jsonify, request, session, current_app
from functools import wraps
import requests, csv

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

@app.route('/watch_list', methods=['GET', 'POST'])
@login_required
def watch_list(): 
    if request.method == 'POST':
        username = request.form.get('username')
        movie_title = request.form.get('movie_title')  
        movie_year = request.form.get('movie_year')  
        movie_rated = request.form.get('movie_rated')  
        movie_released = request.form.get('movie_released')  
        movie_runtime = request.form.get('movie_runtime')  
        movie_imdb_id = request.form.get('movie_imdb_id')
        
        watch_later = WatchLater.query.filter_by(user_username=username, title=movie_title).first()
        
        if watch_later:
            print('Movie already in user\'s watch later list')
            return jsonify({'success': False})
        else: 
            new_watch_later = WatchLater(
                title=movie_title,
                year=movie_year,
                rated=movie_rated,
                released=movie_released,
                runtime=movie_runtime,
                imdb_id=movie_imdb_id,
                user_username=username
            )
            db.session.add(new_watch_later)
            db.session.commit()
            return jsonify({'success': True})
          
    return render_template('watch_list.html')

@app.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites():
    if request.method == 'POST':
        username = request.form.get('username')
        movie_title = request.form.get('movie_title')  
        movie_year = request.form.get('movie_year')  
        movie_rated = request.form.get('movie_rated')  
        movie_released = request.form.get('movie_released')  
        movie_runtime = request.form.get('movie_runtime')  
        movie_imdb_id = request.form.get('movie_imdb_id')
        
        favorite = Favorite.query.filter_by(user_username=username, title=movie_title).first()
        
        if favorite:
            print('Movie already in user\'s favorites list')
            return jsonify({'success': False})
        else: 
            new_favorite = Favorite(
                title=movie_title,
                year=movie_year,
                rated=movie_rated,
                released=movie_released,
                runtime=movie_runtime,
                imdb_id=movie_imdb_id,
                user_username=username
            )
            db.session.add(new_favorite)
            db.session.commit()
            return jsonify({'success': True})
                
    return render_template('favorites.html')

@app.route('/profile', methods=['GET'])
@login_required
def profile():        
    return render_template('profile.html')

@app.route('/search', methods=['GET'])
@login_required
def search():   
    username = session['username']       
    title = request.args.get('title')    
    
    if title:
        PARAMS = {'apikey': api_key, 't': title, 'plot': 'full'}
        response = requests.get(url=URL, params=PARAMS)
        movie_data = response.json()
        return render_template('search.html', movie_data=movie_data, username=username)
    else:
        return redirect(url_for('home'))
    
@app.route('/search_suggestions', methods=['GET'])
def search_suggestions():
    names = []
    with open('static/data/movies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Check if the row is not empty
                names.append(row[0])
    return jsonify(names)

if __name__ == "__main__":
    # only run when initially setting up tables for the db
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(debug=True)