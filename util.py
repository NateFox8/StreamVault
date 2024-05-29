import requests
import tmdbsimple as tmdb
from api_keys import *

tmdb.API_KEY = TMBD_KEY

def get_movie_data(title):
    PARAMS = {'apikey': OMDB_KEY, 't': title, 'plot': 'full'}
    response = requests.get(url=OMDB_URL, params=PARAMS)
    movie_data = response.json()
    return movie_data

def get_imdb_id(title):
    movie_data = get_movie_data(title)
    return movie_data['imdbID']

def get_movie_id(title):
    imdb_id = get_imdb_id(title)
    external_source = 'imdb_id'
    find = tmdb.Find(imdb_id)
    find.info(external_source=external_source)
    return find.movie_results[0]['id']

def get_watch_providers(movie_id):
    movie = tmdb.Movies(movie_id)
    return movie.watch_providers()