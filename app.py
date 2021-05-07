from application import app, db
from application.models import Review
from flask import render_template, url_for


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')