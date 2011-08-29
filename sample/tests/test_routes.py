from test_base import TestCrazyHorseBase
import unittest

class TestCrazyHorseRoutes(TestCrazyHorseBase):

    def test_foo(self):
        #print("TestCrazyHorseRoutes: " + str(self))
        test_environ        = {"PATH_INFO": "/nano",
                               "REQUEST_METHOD": "GET",
                               "HTTP_USER_AGENT": "Unknown",
                               "HTTP_ACCEPT":"text/html",
                               'QUERY_STRING': '&id=12&lucy=dog',
                               "HTTP_ACCEPT_LANGUAGE":"en-US",
                               "HTTP_ACCEPT_CHARSET":"utf-8",
                               "REMOTE_ADDR":"127.0.0.1"}
        test_start_response = lambda x,y: x
        self.application(test_environ, test_start_response)
        self.assertTrue(True)