import urlparse
from crazyhorse.features.requests.mime_multipart import parse_mime_multipart
class FormParser(object):

    def __init__(self):
        self.files = None

    def parse_body(self, content_type, length, data):
        if length > 0:

            if content_type.startswith("application/x-www-form-urlencoded"):
                return self._parse_urlencoded(length, data)

            elif content_type.startswith("multipart/form-data"):
                # boundary= is at the end of the content_type, so
                # start looking for the 1st = from the end of the string
                index      = content_type.rfind("=") + 1
                boundary   = content_type[index:]
                params     = self._parse_multipart(length, data, boundary)
                self.files = params["files"]
                return params["data"]

        return {}

    def _parse_urlencoded(self, length, data):
        body = data.read(length)
        return urlparse.parse_qs(body)

    def _parse_multipart(self, length, data, boundary):
        print("MULTIPAT")
        body   = data.read(length)
        return parse_mime_multipart(boundary, body)