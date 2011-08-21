import glob
import os
from crazyhorse.web import routing
from crazyhorse.web import exceptions
from crazyhorse.web.httpcontext import HttpContext
from crazyhorse.web.config import CrazyHorseConfig
from crazyhorse.web.controller import CrazyHorseController

class Application(object):
    def __init__(self, application=None):

        #self.router         = options["router"]() if "router" in options else None
        #self.authorization  = options["authorization"]() if "authorization" in options else None
        #self.sessions       = options["sessions"] if "sessions" in options else None
        #self.cookies        = options["cookies"] if "cookies" in options else None
        #self.request_parser = options["request_parser"] if "request_parser" in options else None
        #self.views          = options["views"] if "views" in options else None


        # fire it up!
        config      = CrazyHorseConfig()
        self.router = routing.application_router

        self.initialize_application_settings(config)
        self.initialize_application_handlers(config)
        self.initialize_application_server_errors(config)
        self.process_orphaned_routes()

        if application is not None:
            application.application_start()

    def process_orphaned_routes(self):
        if len(routing.temp_routes) > 0:
            for route_name in routing.temp_routes:
                try:
                    route = self.router.route_with_name(route_name)
                    for method in routing.temp_routes[route_name]:
                        controller, action  = routing.temp_routes[route_name][method]
                        route.register_action_for_method(method, controller, action)
                except:
                    temp_route = routing.temp_routes[route_name]
                    for key in temp_route.iterkeys():
                        print("Failed to register route for with name: {0} for {1}::{2}".format(route_name, temp_route[key][0], temp_route[key][1]))

        del routing.temp_routes
        #routing.temp_routes = None

    def initialize_application_server_errors(self, config):
        #error is an ElementTree.Element

        for error in config.server_errors.errors:
            controller = error.findtext("controller")
            action     = error.findtext("action")
            code       = error.attrib["code"]
            method     = error.attrib["method"]

            route      = None
            try:
                route  = self.router.routes_available[code]
            except:
                route = routing.Route()
                self.router.routes_available[code] = route

            if method == "*":
                route.register_action_for_method("*", controller, action)
            else:
                method_list = method.split(",")
                for target_method in method_list:
                    route.register_action_for_method(target_method, controller, action)

    def initialize_application_handlers(self, config):
        pass

    def initialize_application_settings(self, config):
        view_path        = config.settings["view"]
        controllers_path = config.settings["controllers"].replace(".", "/")

        #process view
        parts            = view_path.split(".")
        view_classname   = parts.pop()
        view_module_path = ".".join(parts)
        view_module      = __import__(view_module_path, globals(), locals(), [view_classname])
        view_class       = getattr(view_module, view_classname)
        CrazyHorseController.view_class = view_class

        #process controllers
        for file_path in glob.iglob("{0}/*.py".format(controllers_path)):

            if os.path.basename(file_path).startswith("__"): continue

            file_path     = os.path.splitext(file_path)[0]
            module_path   = file_path.replace("/", ".")
            module        = __import__(module_path, globals(), locals())


    def __call__(self, environ, start_response):

            request_handlers = {}
            route            = None
            context          = HttpContext(environ, start_response)

            try:
                route = self.router.route_for_path(context.request.path)
            except (exceptions.InvalidRoutePathException):
                try:
                    route = self.router.route_with_name("404")
                except:
                    start_response("404 NOT FOUND", [])
                    return []

            try:
                route(context)
            except (exceptions.RouteExecutionException):
                start_response("404 NOT FOUND", [])
                return []
            #context.request     = Request(environ, request_handlers)
            #context.response    = Response(start_response)
            start_response("200 OK", [])
            return ["It Works!"]

            handlers = {"environ":environ,
                        "request_parser": self.request_parser,
                        "cookies":self.cookies,
                        "session":self.sessions}

            context             = HttpContext()
            context.request     = Request(**handlers)
            context.response    = Response(start_response, self.cookies)
            context.session     = None if self.sessions is None else  self.sessions(context.request)
            context.view_engine = self.views
            context.environ     = environ

            result = None
            route  = self.router.fetch_route(context)

            #if route.controller.requires_authorization and self.authorization is not None:
            #    if self.authorization.request_is_authorized(request) is False:


            if route is not None:
                route.context = context
                result = route()
            else:
                return
            return context.response(session=context.session, result=result)