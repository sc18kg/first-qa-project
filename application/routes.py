from application import app, db
from application.models import Review, Film
from flask import render_template, url_for
from flask import redirect, request
from application.forms import AddReview, AddFilm


@app.route('/', methods=['GET','POST'])

@app.route('/home', methods=['GET','POST'])
def home():
    all_reviews = Review.query.all()
    all_film = Film.query.all()
    print(all_reviews)
    return render_template('home.html',  title="Home", all_reviews=all_reviews, all_film=all_film)

@app.route('/addfilm', methods=['GET', 'POST'])
def addfilm():
    form = AddFilm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_film = Film(
                title = form.title.data,
                description = form.description.data,
                released_at = form.released_at.data,
                age_rating = form.age_rating.data
            )

        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('addfilm.html', title="Add a Film", form=form)


@app.route('/addreview', methods=['GET','POST'])
def addreview():
    form = AddReview()
    form.film_title.choices = [(film.id, film.title) for film in Film.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            new_review = Review(
                film_id = form.film_title.data,
                author = form.author.data,
                review = form.review.data,
                rating = form.rating.data
            )

        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add_review.html', title='Add a Review', form=form)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = AddReview()
    form.film_title.choices = [(title.title) for title in Film.query.all()]
    review = Review.query.filter_by(id=id).first()
    if request.method == "POST":
        review.film_title = form.film_title.data
        review.author = form.author.data
        review.review = form.review.data
        review.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Review", review=review)

@app.route('/deletereview/<int:id>', methods=["GET", "POST"])
def deletereview(id):
    reviewtodelete = Review.query.get(id)
    db.session.delete(reviewtodelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/deletefilm/<int:id>', methods=["GET", "POST"])
def deletefilm(id):
    filmtodelete = Film.query.get(id)
    db.session.delete(filmtodelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/filmlist', methods=['GET','POST'])
def filmlist():
    all_films = Film.query.all()
    print(all_films)
    return render_template("filmlist.html", title="Film List", all_films=all_films)

@app.route('/count', methods=["GET", "POST"])
def count():
    number_of_reviews = Review.query.count()
    print(number_of_reviews)
    db.session.commit()
    return render_template("count.html", title="Count", number_of_reviews=number_of_reviews)