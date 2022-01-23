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

    @classmethod
    def setUpClass(cls):
        # 각 테스트클래스가 실행될때마다 딱 한 번씩만 실행
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['DEBUG'] = False
        app.config['PROPAGATE_EXCEPTIONS'] = True
        with app.app_context():
            db.init_app(app)
            # db.create_all()

    def setUp(self):
        # make sure database exits
        # 각 테스트 클래스의 메소드가 실행될때마다 한 번씩만 실행
        with app.app_context():
            db.create_all()
        # Get a test clinet
        self.app = app.test_client
        self.app_context = app.app_context()  # 앱에 관련된 모든 정보들을 가져옴.

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
