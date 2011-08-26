class Application(object):

    def __init__(self, application=None):
        #self.router         = options["router"]() if "router" in options else None
        #self.authorization  = options["authorization"]() if "authorization" in options else None
        #self.sessions       = options["sessions"] if "sessions" in options else None
        #self.cookies        = options["cookies"] if "cookies" in options else None
        #self.request_parser = options["request_parser"] if "request_parser" in options else None
        #self.views          = options["views"] if "views" in options else None


        # fire it up!
        crazyhorse.get_logger().info("Initializing CrazyHorse")
        Configuration()

        if application is not None:
            application_start = getattr(application, "application_start", None)

            if application_start:
                crazyhorse.get_logger().debug("Executing custom application_start")
                application_start()