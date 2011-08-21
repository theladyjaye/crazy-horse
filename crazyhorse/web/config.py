import os
import json
from xml.etree import ElementTree

class CrazyHorseSettings(object):

    def __init__(self):
        self.node = None

    def __get__(self, instance, owner):
        if self.node is None:
            self.node = instance.parser["settings"]

        return self

    def __getitem__(self, index):
        return self.node[index]

class CrazyHorseHandlers(object):

    def __init__(self):
        self.node = None

    def __get__(self, instance, owner):
        if self.node is None:
            self.node = instance.parser["handlers"]

        return self

    def __getitem__(self, index):
        return self.node[index]

class CrazyHorseServerErrors(object):

    def __init__(self):
        self.node = None

    def __get__(self, instance, owner):
        if self.node is None:
            self.node = instance.parser["server_errors"]

        return self

    @property
    def errors(self):
        return self.node["errors"]

class CrazyHorseConfig(object):
    settings      = CrazyHorseSettings()
    handlers      = CrazyHorseHandlers()
    server_errors = CrazyHorseServerErrors()

    def __init__(self):
        #self.parser   = ElementTree.parse(os.getcwd() + "/crazyhorse.config")
        config_json = open(os.getcwd() + "/crazyhorse.config")
        self.parser = json.load(config_json)

