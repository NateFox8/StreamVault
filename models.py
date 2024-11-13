from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
import uuid

# The db object instantiated from the class SQLAlchemy represents the database and
# provides access to all the functionality of Flask-SQLAlchemy
db = SQLAlchemy()

# create tables for db
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    username = db.Column(db.String(20), unique=True, primary_key=True)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    
    # unique keys
    watch_later = db.relationship('WatchLater', backref='user')
    favorites = db.relationship('Favorite', backref='user')    
    rates = db.relationship('Rate', backref='user')    
    
    def __repr__(self):
        return '<User %r>' % self.username
    
class WatchLater(db.Model):
    __tablename__ = 'watch_later'
    
    watch_later_id = db.Column(db.String(36), primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(20))
    year = db.Column(db.String(4))
    rated = db.Column(db.String(4))
    released = db.Column(db.String(12))
    runtime = db.Column(db.String(10))
    
    user_username = db.Column(db.String(20), db.ForeignKey('users.username'))    
    
    def __repr__(self):
        return '<WatchLater %r>' % self.watch_later_id
    
class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    favorite_id = db.Column(db.String(36), primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(20))
    year = db.Column(db.String(4))
    rated = db.Column(db.String(4))
    released = db.Column(db.String(12))
    runtime = db.Column(db.String(10))
    
    user_username = db.Column(db.String(20), db.ForeignKey('users.username'))    
    
    def __repr__(self):
        return '<Favorite %r>' % self.favorite_id
    
class Rate(db.Model):
    __tablename__ = 'rates'
    
    rate_id = db.Column(db.String(36), primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(20))
    rate = db.Column(db.Integer)
    year = db.Column(db.String(4))
    
    user_username = db.Column(db.String(20), db.ForeignKey('users.username'))    
    
    def __repr__(self):
        return '<Rate %r>' % self.rate_id