import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Review, Film 
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI= getenv('DATABASE_URI'),# = "sqlite:///data6.db"
                SECRET_KEY=getenv('SECRET_KEY'),
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        
        new_film = Film(title='The Conjuring', description='Scary film, very creepy', released_at=2018, age_rating='18')
        db.session.add(new_film)
        db.session.commit()

        new_review = Review(author='Micheal Bob', review='Great film', id=new_film.id, rating='9')
        db.session.add(new_review)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_addfilm_get(self):
        response = self.client.get(url_for('addfilm'))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('addreview'))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('updatefilm', id=1))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('deletereview', id=1))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('deletefilm', id=1))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('filmlist'))
        self.assertEqual(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get(url_for('count'))
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):

    def test_addfilm(self):
        response = self.client.post(
            url_for('addfilm'),
            data = dict(
		        title='Marley and Me',
		        description='Film about a man and his best friend',
		        released_at='2006'
            ),
            follow_redirects=True
        )
        self.assertIn(b'Marley and Me',response.data)

    def test_addreview(self):
        response = self.client.post(
            url_for('addreview'),
            data = dict(
                film_title=1,
		        author='Shia Lebouf',
		        review='Very good film but also a tear jerker',
		        rating='10'),
                follow_redirects=True
        )
        self.assertIn(b'Shia Lebouf',response.data)

class TestUpdate(TestBase):

    def test_updatefilm(self):
        response = self.client.post(
            'updatefilm/1',
            data = dict(
		title='Thor',
		description='Mighty god of thunder kicks enemy behinds',
        released_at='2004',
		age_rating=12
		),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

    def test_updatereview(self):
        response = self.client.post(
            'update/1',
            data = dict(
		author='Billy Bighead',
		review='Great watch a cinematic masterpiece',
		rating='8'
		),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

class TestDelete(TestBase):
       def test_deletefilm(self):
        response = self.client.get(
            'deletefilm/1'
            )
        self.assertEqual(response.status_code,302)

       def test_deletereview(self):
         response = self.client.get(
                'deletereview/1'
            )
         self.assertEqual(response.status_code,302) 