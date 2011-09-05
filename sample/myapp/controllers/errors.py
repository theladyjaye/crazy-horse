from crazyhorse.web.controller import CrazyHorseController
class ServerErrorController(CrazyHorseController):

    def error_404(self):
        model = {"message":"There was an error"}
        return self.redirect("/about/1234/archive")

    def error_500(self):
        model = {"message":"There was an error"}
        return self.view("generic_500", model)