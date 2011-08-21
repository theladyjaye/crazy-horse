from crazyhorse.web.views import CrazyHorseView

class CrazyHorseController(object):
    view_class = None

    def __init__(self):
        self.httpcontext = None

    def initialize(self):pass

    def redirect(self, url):
        pass

    def view(self, *args, **kwargs):
        return CrazyHorseController.view_class(*args, **kwargs)
