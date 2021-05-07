from application import app, db
from application.models import Review
from flask import render_template, url_for
from flask import redirect, request
from application.forms import AddReview


@app.route('/', methods=['GET','POST'])

@app.route('/home', methods=['GET','POST'])
def home():
    all_reviews = Review.query.all()
    print(all_reviews)
    return render_template('home.html',  title="Home", all_reviews=all_reviews)

@app.route('/addreview', methods=['GET','POST'])
def addreview():
    form = AddReview()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_review = Review(
                film_title = form.film_title.data,
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
    review = Review.query.filter_by(id=id).first()
    if request.method == "POST":
        review.film_title = form.film_title.data
        review.author = form.author.data
        review.review = form.review.data
        review.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Review", review=review)

@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    reviewtodelete = Review.query.get(id)
    
    db.session.delete(reviewtodelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/about', methods=['GET','POST'])
def about():
    
    return render_template("about.html", title="About")

@app.route('/count', methods=["GET", "POST"])
def count():
    number_of_tasks = Review.query.count()
    db.session.commit()
    return render_template("count.html", title="Count")