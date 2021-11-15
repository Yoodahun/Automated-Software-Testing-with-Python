from unittest import TestCase
from app import app


class BaseTest(TestCase):
    #test
    def setUp(self):
        app.testing = True
        self.app = app.test_client
