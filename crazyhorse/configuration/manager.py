from __future__ import absolute_import
import os
import json
import importlib
import collections
import crazyhorse
from crazyhorse.configuration.application import ApplicationSection
from crazyhorse.configuration.crazyhorse import CrazyHorseSection
from crazyhorse.utils.tools import import_class

class Configuration(object):

    SETTINGS = None

    def __init__(self):
        config_json = open(os.getcwd() + "/crazyhorse.config")
        config      = json.load(config_json)
        self.initialize_sections(config)


    def initialize_sections(self, config):
        application_section = ApplicationSection()
        crazyhorse_section  = CrazyHorseSection()

        Configuration.SETTINGS = application_section(config["application"])
        crazyhorse_section(config["crazyhorse"])

        if "custom_sections" in config:
            for custom_section in config["custom_sections"]:
                self.initialize_custom_section(config, custom_section)

    def initialize_custom_section(self, config, meta):

        name    = meta["name"]
        pkg     = meta["type"]
        cls     = import_class(pkg)
        obj     = None
        section = None

        crazyhorse.get_logger().info("Processing {0} Configuration".format(cls.__name__))

        if name in config:
            section = config[name]

        obj = cls()

        if section:
            setattr(Configuration, name.upper(), obj(section))
        else:
            setattr(Configuration, name.upper(), obj())
