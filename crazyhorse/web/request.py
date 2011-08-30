
class Request(object):

    def __init__(self, environ):

        #TODO
        # Cookie parsing
        # Request Data parsing
        self.environment    = environ
        self.path           = environ["PATH_INFO"]
        self.request_method = environ.get("REQUEST_METHOD", "GET").upper()
        self.user_agent     = environ.get("HTTP_USER_AGENT", "Unknown")
        self.accepts        = environ.get("HTTP_ACCEPT", "text/plain")
        self.language       = environ.get("HTTP_ACCEPT_LANGUAGE", "en-US")
        self.charset        = environ.get("HTTP_ACCEPT_CHARSET", "utf-8")
        self.remote_address = environ.get("REMOTE_ADDR", "0.0.0.0")

        self.querystring    = None
        self.cookies        = None
        self.session        = None
        self.params         = None
        self.files          = None
        self.headers        = None