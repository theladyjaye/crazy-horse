import crazyhorse
from crazyhorse.configuration.manager import Configuration
from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web.response import Response
from crazyhorse.web import exceptions
from crazyhorse.web import routing

class Application(object):

    def __init__(self, application=None):
        #self.router         = options["router"]() if "router" in options else None
        #self.authorization  = options["authorization"]() if "authorization" in options else None
        #self.sessions       = options["sessions"] if "sessions" in options else None
        #self.cookies        = options["cookies"] if "cookies" in options else None
        #self.request_parser = options["request_parser"] if "request_parser" in options else None


        # fire it up!
        crazyhorse.get_logger().info("Initializing CrazyHorse")
        crazyhorse.get_logger().debug("Processing Configuration")
        Configuration()

        if application is not None:
            application_start = getattr(application, "application_start", None)

            if application_start:
                crazyhorse.get_logger().debug("Executing custom application_start")
                application_start()



    def failure(self, start_response):
        start_response("404 NOT FOUND", [])
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
                    return self.failure(start_response)


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

            #start_response("200 OK", [])
            #return ["It Works!"]

            result = None

            #if route.controller.requires_authorization and self.authorization is not None:
            #    if self.authorization.request_is_authorized(request) is False:


            if route is not None:
                try:
                    result = route(context)
                except exceptions.RouteExecutionException:
                    return self.failure(start_response)
            else:
                return self.failure(start_response)
            
            return context.response(session=context.session, result=result)