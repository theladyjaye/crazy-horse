import re
from crazyhorse.web import exceptions

def register_route(name, controller, action, path, method="GET", constraints=None):
    route = Route(path, constraints)
    route.register_action_for_method(method, controller, action)
    application_router.add_route(name, route)
    return route


class Router(object):

    def __init__(self):
        self.route_table      = []
        self.routes_available = {}

    def add_route(self, name, route):
        """Add a route to the respective route collections"""
        if name not in self.routes_available:
            self.routes_available[name] = route
            self.route_table.append(route)
        else:
            raise exceptions.DuplicateRouteNameException(name)

    def route_with_name(self, route_name):
        """Find a route based on the provided name"""
        try:
            route = self.routes_available[route_name]
        except:
            raise exceptions.InvalidRouteNameException(route_name)

        return route

    def route_for_path(self, path):
        """Find a route based on the provided path, ignores query string values"""
        route = None

        for candidate in self.route_table:
            if candidate.pattern.match(path):
                route = candidate
                break

        if route is None:
            raise exceptions.InvalidRoutePathException(path)

        return route


class Route(object):
    params_test = re.compile(r"\{([a-zA-Z0-9]+)\}")

    def __init__(self, path=None, constraints=None):
        self.actions    = {}
        self.pattern    = None
        self.params     = None
        self.path       = path

        if path is not None:
            pattern         = None
            params          = None

            if Route.params_test.search(path):
                params  = tuple(Route.params_test.findall(path))
                if constraints is not None:
                    pattern = path
                    for key in Route.params_test.findall(path):
                        if key in constraints:
                            pattern = re.sub(r"{" + key + r"}", "(" + constraints[key] + ")", pattern )
                else:
                    pattern = Route.params_test.sub(r"([^/]+)", path)
            else:
                pattern = path

            self.pattern = re.compile("^" + pattern + "$")
            if params is not None: self.params = params

    def register_action_for_method(self, method, controller, action, temp=False):
        method = method.upper().strip()
        self.actions[method] = (controller, action)

    def action_with_method(self, method):
        try:
            return self.actions[method]
        except KeyError as e:
            if "*" in self.actions:
                return self.actions["*"]
            else:
                if "GET" in self.actions:
                    return self.actions["GET"]
                else:
                    raise e

    def __call__(self, httpcontext):
        method     = httpcontext.request.request_method
        controller = None
        action     = None
        klass      = None

        try:
            controller, action = self.action_with_method(method)
        except KeyError:
            # no specific controller/action combo existed for the method 404 it
            try:
                route = application_router.route_with_name("404")
                try:
                    route.action_with_method("404")
                except KeyError:
                    raise exceptions.RouteExecutionException()
            except (exceptions.InvalidRouteNameException):
                raise exceptions.RouteExecutionException()

        if controller not in route_controller_registry:
            parts       = controller.split(".")
            classname   = parts.pop()
            module_path = ".".join(parts)


            module      = __import__(module_path, globals(), locals(), [classname])
            klass       = getattr(module, classname)
            route_controller_registry[controller] = klass
        else:
            klass = route_controller_registry[controller]

        params = {}

        if self.params:
            result = self.pattern.match(httpcontext.request.path)
            params = dict(zip(self.params, result.groups()))

        obj    = klass()
        method = getattr(obj, action)
        method(**params)

temp_routes               = {}
route_controller_registry = {}
application_router        = Router();