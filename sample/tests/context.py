class TestContext(object):

    @classmethod
    def default_context(cls):
         return {'wsgi.multiprocess': False,
                 'REQUEST_METHOD': 'GET',
                 'PATH_INFO': '/foo.bar/baz/nanobot',
                 'SERVER_PROTOCOL': 'HTTP/1.1',
                 'QUERY_STRING': '&id=12',
                 'CONTENT_LENGTH': '',
                 'HTTP_ACCEPT_CHARSET':
                 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1',
                 'HTTP_CONNECTION': 'keep-alive',
                 'SERVER_NAME': 'rodeo',
                 'REMOTE_ADDR': '127.0.0.1',
                 'wsgi.url_scheme': 'http',
                 'SERVER_PORT': '80',
                 'x-wsgiorg.uwsgi.version': '0.9.6.2',
                 'DOCUMENT_ROOT': '/usr/local/Cellar/nginx/1.0.2/html',
                 'wsgi.input': <open file 'wsgi_input', mode 'r' at 0x10110b4b0>,
                 'HTTP_HOST': 'rodeo',
                 'wsgi.multithread': False,
                 'REQUEST_URI': '/foo.bar/baz/nanobot?&id=12',
                 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                 'wsgi.version': (1, 0),
                 'wsgi.run_once': False,
                 'wsgi.errors': <open file 'wsgi_input', mode 'w' at 0x101231150>,
                 'REMOTE_PORT': '55322',
                 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8',
                 'CONTENT_TYPE': '',
                 'wsgi.file_wrapper': <built-in function uwsgi_sendfile>,
                 'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch'}

    def __init__(self):
        pass


