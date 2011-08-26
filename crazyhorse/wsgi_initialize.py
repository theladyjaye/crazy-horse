import crazyhorse

from crazyhorse.web.config import CrazyHorseConfig
from crazyhorse.web import routing
from crazyhorse.web import exceptions

class ApplicationInitialize(object):

    def initialize_application(self):
        config      = CrazyHorseConfig()
        self.router = routing.application_router

        self.initialize_application_settings(config)
        self.initialize_application_handlers(config)
        self.initialize_application_server_errors(config)
        self.process_orphaned_routes()

    def initialize_application_handlers(self, config):
        pass

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
                        crazyhorse.get_logger().warning("Failed to register route for with name: {0} for {1}::{2}".format(route_name, temp_route[key][0], temp_route[key][1]))

        del routing.temp_routes
        #routing.temp_routes = None

    def initialize_application_server_errors(self, config):
        #error is an ElementTree.Element

        for error in config.server_errors.errors:
            controller = error["controller"]
            action     = error["action"]
            code       = error["code"]
            method     = error["method"]

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
