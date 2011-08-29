from __future__ import absolute_import
import crazyhorse
from crazyhorse.web import exceptions
from crazyhorse.configuration.sections import ConfigurationSection
from crazyhorse.utils.tools import import_class

class CrazyHorseSection(ConfigurationSection):

    def __init__(self):
        pass

    def initialize_features(self, section):
        result = {}

        #if "cookies" in section:
            #result["cookies"] = self.initialize_cookie_handler(section["cookies"])

        if "querystrings" in section:
            result["querystrings"] = self.initialize_querystring_handler(section["querystrings"])

        return result


    def initialize_cookie_handler(self, pkg):
        cls = import_class(pkg)
        return cls()

    def initialize_querystring_handler(self, pkg):
        cls = import_class(pkg)
        return cls

    def __call__(self, section):
        crazyhorse.get_logger().debug("Processing CrazyHorse Configuration")
        features = None

        try:
            features = self.initialize_features(section["features"])
        except KeyError:
            crazyhorse.get_logger().fatal("No crazyhorse handlers defined in config")
            raise exceptions.ConfigurationErrorException("No crazyhorse handlers defined in config")

        return features
