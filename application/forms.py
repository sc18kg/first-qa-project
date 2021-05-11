from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class AddReview(FlaskForm):
    
    film_title = SelectField("Film Title:",choices=[])
    author = StringField("Reviewee Name:")
    review = StringField("Review:")
    rating = StringField("What was your rating /10:")
    submit = SubmitField("Submit Task")

class AddFilm(FlaskForm):

    title = StringField("Film Title: ")
    description = StringField("Description: ")
    released_at = StringField("Release date:")
    age_rating = SelectField("Age Rating",
            choices=[("U","U"),
                    ("PG","PG"),
                    ("12A","12A"),
                    ("12","12"),
                    ("15","15"),
                    ("18","18")
                ]
            )
    submit = SubmitField("Add The Film")