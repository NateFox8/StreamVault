import requests
import tmdbsimple as tmdb
from api_keys import *

tmdb.API_KEY = TMBD_KEY
POSTER_URL = 'https://image.tmdb.org/t/p/w185/'

def get_omdb_movie_data(title):
    PARAMS = {'apikey': OMDB_KEY, 't': title, 'plot': 'full'}
    response = requests.get(url=OMDB_URL, params=PARAMS)
    movie_data = response.json()
    return movie_data

def get_tmdb_movie_data(title):
    movie = tmdb.Movies(get_movie_id(title))    
    return(movie.info()) 

def get_movie_id(title):
    search = tmdb.Search()
    search.movie(query=title)
    return search.results[0]['id']

def get_watch_providers(title):
    movie = tmdb.Movies(get_movie_id(title))
    watch_providers = movie.watch_providers()['results']['US']
    
    buy_options = {}
    rent_options = {}
    flatrate_options = {}

    for category, providers in watch_providers.items():
        if category == 'buy':
            buy_options[category] = providers
        elif category == 'rent':
            rent_options[category] = providers
        elif category == 'flatrate':
            flatrate_options[category] = providers

    return buy_options, rent_options, flatrate_options

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