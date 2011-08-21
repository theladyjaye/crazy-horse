from crazyhorse.web.application import CrazyHorseApplication

class MyApp(CrazyHorseApplication):

  def application_start(self):
    print("application start")