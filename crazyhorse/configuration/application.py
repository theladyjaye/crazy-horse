from __future__ import absolute_import
import crazyhorse
from crazyhorse.configuration.sections import ConfigurationSection


class ApplicationSection(ConfigurationSection):

    def __init__(self):
        pass

    def initialize_system(self, section):
        pass
        #print(section)

    def initialize_custom_errors(self, section):
        pass

    def __call__(self, section):
        crazyhorse.get_logger().info("Processing Application Configuration")
        settings = None

        try:
            self.initialize_system(section["system"])
        except KeyError:
            pass
            # no system section was defined
            # TODO throw a meaningful exception

        if "settings" in section:
            settings = section["settings"]

        if "custom_errors" in section:
            self.initialize_custom_errors(section["custom_errors"])

        return settings