import unittest
import os
from crazyhorse import wsgi
class TestCrazyHorseBase(unittest.TestCase):
    application = None

    @classmethod
    def setUpClass(cls):
        if cls.application == None:
          cls.application = wsgi.Application()

    def application(self, environ, start_response):
        TestCrazyHorseBase.application(environ, start_response)

    def setUp(self):
        pass