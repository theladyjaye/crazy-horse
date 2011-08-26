from __future__ import absolute_import
import crazyhorse
from crazyhorse.configuration.sections import ConfigurationSection

class CrazyHorseSection(ConfigurationSection):

    def __init__(self):
        pass

    def initialize_handlers(self, section):
        #print(section)
        pass

    def __call__(self, section):
        crazyhorse.get_logger().info("Processing CrazyHorse Configuration")
        if "handlers" in section:
            self.initialize_handlers(section["handlers"])

        return None
