from __future__ import absolute_import
import crazyhorse
from crazyhorse.web import exceptions
from crazyhorse.configuration.sections import ConfigurationSection

class CrazyHorseSection(ConfigurationSection):

    def __init__(self):
        pass

    def initialize_handlers(self, section):
        #print(section)
        pass

    def __call__(self, section):
        crazyhorse.get_logger().debug("Processing CrazyHorse Configuration")

        try:
            self.initialize_handlers(section["handlers"])
        except KeyError:
            crazyhorse.get_logger().fatal("No crazyhorse handlers defined in config")
            raise exceptions.ConfigurationErrorException("No crazyhorse handlers defined in config")

        return None
