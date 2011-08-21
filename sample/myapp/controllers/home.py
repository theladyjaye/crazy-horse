from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.actions import route
class HomeController(CrazyHorseController):

    @route(name        = "Home",
           path        = "/")
    def index(self):
        print "HOME!"
