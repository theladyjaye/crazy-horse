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
        #self.params         = RequestParams({})
        #self.files          = RequestParams({})

        #self.cookies = None if cookies is None else cookies(environ.get("HTTP_COOKIE", None))

        #content_length = -1
#
        #try:
        #    content_length = int(environ.get("CONTENT_LENGTH", "0"))
        #except ValueError, e: pass
#
#
        #if request_parser:
#
        #    parser = request_parser()
#
        #    querystring = parser.parse_querystring(environ["QUERY_STRING"])
        #    self.params.update(querystring)
#
#
        #    if content_length > 0:
        #        values = {"content_type":environ.get("CONTENT_TYPE", "application/unknown"),
        #                  "length": content_length,
        #                  "data":environ["wsgi.input"]}
#
        #        # merge a dictionary:
        #        # http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-as-a-single-expression
        #        body = parser.parse_body(**values)
        #        self.params.update(body)
#
        #        if len(parser.files) > 0:
        #            self.files.update(parser.files)