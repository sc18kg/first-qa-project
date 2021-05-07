from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class AddReview(FlaskForm):
    
    film_title = StringField("Film Title:")
    author = StringField("Reviewee Name:")
    review = StringField("Review:")
    rating = StringField("What was your rating /10:")
    submit = SubmitField("Submit Task")
