from crazyhorse.configuration.sections import ConfigurationSection
class TestSection(ConfigurationSection):

    def __init__(self):
        pass

    def __call__(self, section=None):
        return section