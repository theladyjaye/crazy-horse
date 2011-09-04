import crazyhorse
from crazyhorse.configuration.manager import Configuration
from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web.response import Response
from crazyhorse.web import exceptions
from crazyhorse.web import routing

class Application(object):

    def __init__(self, application=None):
        
        # fire it up!
        crazyhorse.get_logger().info("Initializing CrazyHorse")
        crazyhorse.get_logger().debug("Processing Configuration")
        Configuration()

        if application is not None:
            application_start = getattr(application, "application_start", None)

            if application_start:
                crazyhorse.get_logger().debug("Executing custom application_start")
                application_start()



    def error_404(self, start_response):
        start_response("404 NOT FOUND", [])
        return []
    
    def error_500(self, start_response):
        start_response("500 INTERNAL SERVER ERROR", [])
        return []

    def __call__(self, environ, start_response):
            request_handlers = {}
            route            = None
            context          = None
            path             = environ["PATH_INFO"]
            router           = routing.application_router

            try:
                route = router.route_for_path(path)
            except (exceptions.InvalidRoutePathException):
                try:
                    route = router.route_with_name("404")
                except:
                    return self.error_404(start_response)


            # we have a route object, lets get busy:
            context = HttpContext(environ, start_response)

            # -------- testing stuff
            #print(environ)
            #content_length = -1
            #try:
            #    content_length = int(context.environ.get("CONTENT_LENGTH", "0"))
            #except ValueError:
            #    pass

            #if "wsgi.input" in environ:
            #    print(content_length)
            #    #data = environ["wsgi.input"].read(content_length)
            #    f = open("multipart-request.txt", "wb")
            #    f.write(environ["wsgi.input"].read(content_length))
            # --------

            # apply features
            application_features = Configuration.CRAZYHORSE_FEATURES
            [application_features[x](context) for x in application_features]

            result = None

            
            # TODO I think I can make this nicer
            # Feels a little sloppy to me

            # TODO add hook for authorization/authentication

            if route is not None:
                try:
                    result = route(context)
                except exceptions.RouteExecutionException:
                    return self.error_404(start_response)
            else:
                return self.error_404(start_response)
            try:
                return context.response(session=context.session, result=result)
            except:
                try:
                    route  = router.route_with_name("500")
                    result = route(context)
                    return context.response(session=context.session, result=result)
                except:
                    return self.error_500(start_response)
