import requests
import tmdbsimple as tmdb
from flask import request, jsonify
from keys import *
from models import *

# change value to your TMDB api key
tmdb.API_KEY = TMDB_KEY
POSTER_URL = 'https://image.tmdb.org/t/p/w185/'

# change value to your OMDB api key
OMDB_API_KEY = OMDB_KEY
OMDB_URL = "http://www.omdbapi.com/?"

# functions for general api use

def get_omdb_movie_data(title):
    PARAMS = {'apikey': OMDB_API_KEY, 't': title, 'plot': 'full'}
    response = requests.get(url=OMDB_URL, params=PARAMS)
    movie_data = response.json()
    ratings = movie_data.get('Ratings', [])
    return movie_data, ratings

def get_tmdb_movie_data(title):
    movie = tmdb.Movies(get_movie_id(title))
    return(movie.info()) 

def get_movie_id(title):
    search = tmdb.Search()
    search.movie(query=title)
    return search.results[0]['id']

def get_movie_trailer(title):
    movie = tmdb.Movies(get_movie_id(title))
    videos = movie.videos()

    for video in videos['results']:
        if video['type'].lower() == 'trailer':
            return f"https://www.youtube.com/embed/{video['key']}"

def get_watch_providers(title):
    movie = tmdb.Movies(get_movie_id(title)) 
    
    if movie.watch_providers()['results']:    
        watch_providers = movie.watch_providers()['results']['US']
            
        buy_options = []
        rent_options = []
        flatrate_options = []

        for category, providers in watch_providers.items():
            if category == 'buy':
                for provider in providers:
                    buy_options.append({'provider_name': provider['provider_name'], 'logo_path': provider['logo_path']})
            elif category == 'rent':
                for provider in providers:
                    rent_options.append({'provider_name': provider['provider_name'], 'logo_path': provider['logo_path']})
            elif category == 'flatrate':
                for provider in providers:
                    flatrate_options.append({'provider_name': provider['provider_name'], 'logo_path': provider['logo_path']})

        return buy_options, rent_options, flatrate_options

    return None, None, None

def get_movie_poster(title):
    movie = tmdb.Movies(get_movie_id(title))
    movie.info()
    return movie.poster_path

def get_popular_movies():
    movie = tmdb.Movies()
    movie.popular(language='en')
    movies = [(result['title'], result['poster_path']) for result in movie.results]
    return movies

def get_top_rated_movies():
    movie = tmdb.Movies()
    movie.top_rated(language='en')
    movies = [(result['title'], result['poster_path']) for result in movie.results]
    return movies

def get_popular_tv():
    tv = tmdb.TV()
    tv.popular(language='en')
    shows = [(result['name'], result['poster_path']) for result in tv.results]
    return shows

def get_top_rated_tv():
    tv = tmdb.TV()
    tv.top_rated(language='en')
    shows = [(result['name'], result['poster_path']) for result in tv.results]
    return shows

def get_movie_actors(title):
    base_url = "https://image.tmdb.org/t/p/w500"
    movie = tmdb.Movies(get_movie_id(title))
    actor_names = [actor['name'] for actor in movie.credits()['cast'] if actor['known_for_department'] == 'Acting']
    actor_images = [actor['profile_path'] for actor in movie.credits()['cast'] if actor['known_for_department'] == 'Acting']
    actor_image_urls = [f"{base_url}{path}" for path in actor_images]
    return zip(actor_names, actor_image_urls)
    
    
def get_actor_id(name):
    actor = tmdb.Search()
    actor.person(query=name)
    return actor.results[0]['id']



# functions for database use

def get_watch_later_id(username, title):
    if(WatchLater.query.filter_by(user_username=username, title=title).first()):
        watch_later = WatchLater.query.filter_by(user_username=username, title=title).first()
        return watch_later.watch_later_id
    return None
        
def get_favorite_id(username, title):
    if(Favorite.query.filter_by(user_username=username, title=title).first()):
        favorite = Favorite.query.filter_by(user_username=username, title=title).first()
        return favorite.favorite_id
    return None

def add_watch_later(username, title):
    if get_watch_later_id(username, title):
            print('Movie already in user\'s watch later list')
            return jsonify({'success': False})
    else: 
        new_watch_later = WatchLater(
            title=title,
            year=request.form.get('movie_year'),
            rated=request.form.get('movie_rated'),
            released=request.form.get('movie_released'),
            runtime=request.form.get('movie_runtime'),
            user_username=username
        )
        
        db.session.add(new_watch_later)
        db.session.commit()
        return jsonify({'success': True})

    
def add_favorite(username, title):
    if get_favorite_id(username, title):
            print('Movie already in user\'s favorites list')
            return jsonify({'success': False})
    else: 
        new_favorite = Favorite(
            title=title,
            year=request.form.get('movie_year'),
            rated=request.form.get('movie_rated'),
            released=request.form.get('movie_released'),
            runtime=request.form.get('movie_runtime'),
            user_username=username
        )
        
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({'success': True})