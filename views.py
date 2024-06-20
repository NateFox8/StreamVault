from flask import Blueprint, render_template, redirect, url_for, jsonify, request, session
from models import *
from util import *
from functools import wraps
import csv

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
    movies = get_popular_movies()
    top_rated = get_top_rated_movies()
    return render_template('home.html', movies=movies, top_rated=top_rated)

@views_bp.route('/watch_later', methods=['GET', 'POST'])
@login_required
def watch_later(): 
    if request.method == 'POST':
        username = request.form.get('username')
        movie_title = request.form.get('movie_title')  
               
        watch_later = WatchLater.query.filter_by(user_username=username, title=movie_title).first()
        
        if watch_later:
            print('Movie already in user\'s watch later list')
            return jsonify({'success': False})
        else: 
            new_watch_later = WatchLater(
                title=movie_title,
                year=request.form.get('movie_year'),
                rated=request.form.get('movie_rated'),
                released=request.form.get('movie_released'),
                runtime=request.form.get('movie_runtime'),
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
        
        favorite = Favorite.query.filter_by(user_username=username, title=movie_title).first()
        
        if favorite:
            print('Movie already in user\'s favorites list')
            return jsonify({'success': False})
        else: 
            new_favorite = Favorite(
                title=movie_title,
                year=request.form.get('movie_year'),
                rated=request.form.get('movie_rated'),
                released=request.form.get('movie_released'),
                runtime=request.form.get('movie_runtime'),
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
        buy_options, rent_options, flatrate_options = (get_watch_providers(title))
        omdb_info = get_omdb_movie_data(title)
        tmdb_info = get_tmdb_movie_data(title)
        movie_trailer = get_movie_trailer(title)
        return render_template('search.html', omdb_info=omdb_info, tmdb_info=tmdb_info, buy_options=buy_options, rent_options=rent_options, flatrate_options=flatrate_options,
                               username=username, movie_trailer=movie_trailer)
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