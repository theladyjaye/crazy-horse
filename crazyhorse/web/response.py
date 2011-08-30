#from organism.net.headers import Headers
class Response(object):
    OK                = "200 OK"
    MOVED_PERMANENTLY = "301 Moved Permanently"
    MOVED_TEMPORARILY = "302 Moved Temporarily"
    FORBIDDEN         = "403 Forbidden"
    NOT_FOUND         = "404 Not Found"

    def __init__(self, handler, cookies=None):
        return
        self.handler = handler
        self.status  = Response.OK

        self.headers = Headers()
        self.headers.add("content-type", "text/plain", charset="utf-8")

        self.cookies = None
        self.out     = []

    def write(self, value):
        self.out.append(value)

    def __call__(self, session=None, result=None):
        value = None

        if result is not None:
            value = result()

            if value is not None:
                self.out.append(value.encode("utf-8"))

        if self.cookies is not None and session is not None:
            self.cookies.add(session.key, session.id, path="/")

        if self.cookies is not None and len(self.cookies) > 0:
            for cookie in self.cookies.header_items():
                self.headers.add("Set-Cookie", cookie)

        #self.headers.add("Set-Cookie", "PHPSESSID=ushobtc017r9eibetu6rhnjcm0", path="/")
        self.handler(self.status, self.headers.items())
        return self.out

