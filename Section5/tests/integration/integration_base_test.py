"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that iti is a new, blank database each time.


"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        # make sure database exits
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test clinet
        self.app = app.test_client()
        self.app_context = app.app_context()  # 앱에 관련된 모든 정보들을 가져옴.

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
