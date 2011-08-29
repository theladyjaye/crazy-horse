from crazyhorse.web.request import Request
from crazyhorse.web.response import Response
from crazyhorse.configuration.manager import Configuration

class HttpContext(object):

    def __init__(self, environ, start_response):
        self.request  = Request(environ)
        self.response = Response(start_response)
        self.views    = None
        self.session  = None
        self.environ  = environ

        application_features = Configuration.CRAZYHORSE_FEATURES
        [application_features[x](self) for x in application_features]