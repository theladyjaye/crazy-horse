import inspect
import os
from crazyhorse.web import routing
from crazyhorse.web import exceptions

def route(name, path, method="GET", constraints=None):
    #only way I have currently found to get the class during decoration
    controller    = inspect.stack()[1][3]

    #get rid of the file extension and format the module_path
    file_path     = inspect.stack()[1][1]

    if file_path.startswith("."):
        file_path = file_path[2:]
        file_path = os.path.splitext(file_path)[0]
    else:
        #prefix_length = len(os.getcwd()) + 1
        #had some substring action going on here, but it was breaking: file_path[prefix_length:]
        file_path     = os.path.splitext(file_path)[0]

    module_path   = file_path.replace("/", ".")

    def decorator(f):
        args = {"name"        : name,
                "path"        : path,
                "constraints" : constraints,
                "controller"  : module_path + "." + controller,
                "action"      : f.__name__,
                "method"      : method
                }
        routing.register_route(**args)
        return f
    return decorator

def route_method(method, route_name):
    route          = None
    method         = method
    is_temp_action = False

    #only way I have currently found to get the class during decoration
    controller    = inspect.stack()[1][3]

    #get rid of the file extension and format the module_path
    file_path     = inspect.stack()[1][1]

    if file_path.startswith("."):
        file_path = file_path[2:]
        file_path = os.path.splitext(file_path)[0]
    else:
        #prefix_length = len(os.getcwd()) + 1
        #had some substring action going on here, but it was breaking: file_path[prefix_length:]
        file_path     = os.path.splitext(file_path)[0]

    module_path   = file_path.replace("/", ".")

    try:
        route  = routing.application_router.route_with_name(route_name)
    except (exceptions.InvalidRouteNameException) as e:
        is_temp_action = True

    def decorator(f):
        if is_temp_action:
            if route_name not in routing.temp_routes:
                routing.temp_routes[route_name] = {}
            routing.temp_routes[route_name][method] = (module_path + '.' + controller, f.__name__)
        else:
            route.register_action_for_method(method, module_path + '.' + controller, f.__name__)
        return f

    return decorator
