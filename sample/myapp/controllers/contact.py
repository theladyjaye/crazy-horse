from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.actions import route

class ContactController(CrazyHorseController):

    @route(name        = "contact_index",
           path        = "/contact")
    def index(self):
        model = {"message":"contact"}
        return self.view("contact", model)
