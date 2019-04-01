from OmegaExpansion import relayExp


class Lights(object):

    RELAY_COUNT = 2

    def __init__(self, pin_config):
        self.pin_config = pin_config
        self.setup()

    def setup(self):
        inited = relayExp.checkInit(self.pin_config)
        if not inited:
            relayExp.driverInit(self.pin_config)

    def __getitem__(self, item):
        return relayExp.readChannel(self.pin_config, item)

    def __setitem__(self, item, value):

        if not 0 <= item < self.RELAY_COUNT:
            raise KeyError(item)

        relayExp.setChannel(self.pin_config, item, value)

    def __len__(self):
        return self.RELAY_COUNT
