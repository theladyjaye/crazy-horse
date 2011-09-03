from crazyhorse.web.request import Request
from crazyhorse.web.response import Response

class HttpContext(object):

    def __init__(self, environ, start_response):
        self.path     = environ["PATH_INFO"]
        self.method   = environ.get("REQUEST_METHOD", "GET").upper()
        self.request  = Request(environ)
        self.response = Response(start_response)
        self.views    = None
        self.session  = None
        self.environ  = environ