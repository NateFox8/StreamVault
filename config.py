import os

URL = "http://www.omdbapi.com/?"
api_key = "2265b973"

TMBD_KEY = "f4b52c3670b8f6f64a5b5c1310e0a37e"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNGI1MmMzNjcwYjhmNmY2NGE1YjVjMTMxMGUwYTM3ZSIsInN1YiI6IjY2M2NkZjgyMzMzMjM2ZDg1OWEzYWYwNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.E9n00Hu42cmHNv6796nZ0nqqaiM9Z52dCbV3s-3u5CQ"

class Config:
    SECRET_KEY = 'this_is_the_secret_key'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False