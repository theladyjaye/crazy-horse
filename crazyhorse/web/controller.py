from crazyhorse.web.views import CrazyHorseView

class CrazyHorseController(object):
    view_class = None

    def __init__(self):
        self._current_context = None

    def initialize(self, request):pass

    def current_context(self):
        return self._current_context

    def redirect(self, url):
        pass

    def view(self, *args, **kwargs):
        return CrazyHorseController.view_class(*args, **kwargs)
