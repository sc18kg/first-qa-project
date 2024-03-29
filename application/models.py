from flask_sqlalchemy import SQLAlchemy
from application import db
from datetime import datetime


class Film(db.Model):

    __tablename__ = "Films"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(30), nullable=True)
    description = db.Column(db.String(50), nullable =True)
    released_at = db.Column(db.String(30), nullable=True)
    age_rating = db.Column(db.String(3), nullable=True)
    review = db.relationship('Review', backref='film', passive_deletes=True)

class Review(db.Model):

    __tablename__ = "Review"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('Films.id', ondelete='CASCADE'))
    film_title = db.Column(db.String(30), nullable=True)
    review_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(20), nullable=True)
    review = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Integer, nullable=True)