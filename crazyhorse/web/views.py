
class CrazyHorseView(object):

    def __init__(self, *args, **kwargs):
        self.content_type = "text/plain"

class RedriectView(CrazyHorseView):

    def __call__(self):
        pass