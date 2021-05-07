from flask_sqlalchemy import SQLAlchemy
from application import db
from datetime import datetime


class Film(db.Model):
    """Movie of ratings website"""

    __tablename__ = "Films"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(30), nullable=True)
    description = db.Column(db.String(50), nullable =True)
    released_at = db.Column(db.DateTime, nullable=True)
    age_rating = db.Column(db.Integer, nullable=True)

class Review(db.Model):
    """Rating of ratings website."""

    __tablename__ = "Review"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('Films.id'))
    film_title = db.Column(db.String(30), nullable=True)
    review_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(20), nullable=True)
    review = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
