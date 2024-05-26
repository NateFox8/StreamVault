from flask import Blueprint, render_template, redirect, url_for, jsonify, request, session
from models import *
from api_keys import URL, api_key, TMBD_KEY, ACCESS_TOKEN
from functools import wraps
import requests, csv

views_bp = Blueprint('views', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@views_bp.route('/', methods=['GET'])
@login_required
def index():        
    return redirect(url_for('views.home'))

@views_bp.route('/home', methods=['GET'])
@login_required
def home():        
    return render_template('home.html')

@views_bp.route('/watch_later', methods=['GET', 'POST'])
@login_required
def watch_later(): 
    if request.method == 'POST':
        username = request.form.get('username')
        movie_title = request.form.get('movie_title')  
        movie_year = request.form.get('movie_year')  
        movie_rated = request.form.get('movie_rated')  
        movie_released = request.form.get('movie_released')  
        movie_runtime = request.form.get('movie_runtime')  
        movie_imdb_id = request.form.get('movie_imdb_id')
        poster = request.form.get('poster')
               
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
                poster=poster,
                user_username=username
            )
            db.session.add(new_watch_later)
            db.session.commit()
            return jsonify({'success': True})
        
    username = session['username']       
    watch_later_list = WatchLater.query.filter_by(user_username=username).all()
          
    return render_template('watch_later.html', watch_later_list=watch_later_list)

@views_bp.route('/favorites', methods=['GET', 'POST'])
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
        poster = request.form.get('poster')        
        
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
                poster=poster,
                user_username=username
            )
            db.session.add(new_favorite)
            db.session.commit()
            return jsonify({'success': True})
        
    username = session['username']       
    favorites = Favorite.query.filter_by(user_username=username).all()
                
    return render_template('favorites.html', favorites=favorites)

@views_bp.route('/delete_fav', methods=['POST'])
@login_required
def delete_fav():
    favorite_id = request.form.get('favorite_id')
    favorite = Favorite.query.filter_by(favorite_id=favorite_id).first()
    
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})    

@views_bp.route('/delete_watch_later', methods=['POST'])
@login_required
def delete_watch_later():
    watch_later_id = request.form.get('watch_later_id')
    watch_later = WatchLater.query.filter_by(watch_later_id=watch_later_id).first()
    
    if watch_later:
        db.session.delete(watch_later)
        db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@views_bp.route('/profile', methods=['GET'])
@login_required
def profile():        
    return render_template('profile.html')

@views_bp.route('/search', methods=['GET'])
@login_required
def search():   
    username = session['username']       
    title = request.args.get('title')    
    
    if title:
        PARAMS = {'apikey': api_key, 't': title, 'plot': 'full'}
        response = requests.get(url=URL, params=PARAMS)
        movie_data = response.json()
        print(movie_data)
        return render_template('search.html', movie_data=movie_data, username=username)
    else:
        return redirect(url_for('home'))
    
# @views_bp.route('/search', methods=['GET'])
# @login_required
def tmdb():
    title = request.args.get('title')
    
    if title:
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
        
        headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + ACCESS_TOKEN
        }
                
        response = requests.get(url, headers=headers)  
        movie_data = response.json()
        print(movie_data['results'][0])
        return redirect(url_for('views.home'))      
    else:
        return redirect(url_for('views.home'))
    
@views_bp.route('/search_suggestions', methods=['GET'])
def search_suggestions():
    names = []
    with open('static/data/movies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                names.append(row[0])
    return jsonify(names)