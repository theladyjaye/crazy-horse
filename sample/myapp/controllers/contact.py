from crazyhorse.web.controller import CrazyHorseController
from crazyhorse.web.actions import route
from crazyhorse.web.actions import route_method

class ContactController(CrazyHorseController):

    @route(name        = "contact_index",
           path        = "/contact")
    def index(self):
        model = {"message":"what's up?"}
        return self.view("contact", model)
    
    @route_method("POST","contact_index")
    def submit(self):
        form = self.current_context.request.data
        files = self.current_context.request.files

        name = form["name"]
        model = {"message":name}
        return self.view("contact", model)
