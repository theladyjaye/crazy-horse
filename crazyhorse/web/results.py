from crazyhorse.web.response import Response

class CrazyHorseResult(object):

    def __init__(self, *args, **kwargs):
        self._current_context = None
    
    @property
    def current_context(self):
        return self._current_context
    
    @property
    def content_type(self):
        return "text/plain"

class Redirect(CrazyHorseResult):

    def __init__(self, location):
        self.location = location

    def __call__(self):
        response = self.current_context.response
        response.headers.add("Location", self.location)
        response.status = Response.MOVED_TEMPORARILY
        return None