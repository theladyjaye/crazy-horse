import inspect
import copy
from crazyhorse.web import routing

def override(target, name, method):
    routes = routing.application_router.routes_available
    route  = None

    if target in routes:
        route = copy.copy(routes[target])
    else:
        raise Exception("Invalid route name, unable to locate existing route to override")

    controller = inspect.stack()[1][3] #only way I have currently found to get the class

    def decorator(f):
        route.controller = controller
        route.action     = f.__name__
        routing.application_router.add_route(method, name, route)
        print(routing.application_router.route_table)
        return f

    return decorator

def route(name, path, method="GET", constraints=None):
    controller = inspect.stack()[1][3] #only way I have currently found to get the class
    def decorator(f):
        args = {"name"        : name,
                "path"        : path,
                "constraints" : constraints,
                "controller"  : controller,
                "action"      : f.__name__,
                "method"      : method
                }
        routing.register_route(**args)
        return f

    return decorator