import crazyhorse.wsgi
from myapp.application import MyApp
application = crazyhorse.wsgi.Application(MyApp());