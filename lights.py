import os

import onionGpio


class Lights(object):

    def __init__(self):
        self.relays = {}
        self.switches = {}

        self.setup_gpios(2)

    def setup_gpios(self, count):
        for i in range(count):
            relay_envname = 'RELAY{}'.format(i)
            switch_envname = 'SWITCH{}'.format(i)

            if relay_envname not in os.environ:
                break

            port = int(os.getenv(relay_envname))
            self.relays[i] = onionGpio.OnionGpio(port)
            self.relays[i].setOutputDirection(0)

            if switch_envname in os.environ:
                port = int(os.getenv(switch_envname))
                self.switches[i] = onionGpio.OnionGpio(port)
                self.switches[i].setInputDirection()

    def __getitem__(self, item):
        relay = self.relays.get(item)
        switch = self.switches.get(item)

        if not relay:
            raise KeyError(item)

        if not switch:
            return int(relay.getValue())

        return relay.getValue() ^ switch.getValue()

    def __setitem__(self, item, value):
        relay = self.relays.get(item)
        switch = self.switches.get(item)

        if not relay:
            raise KeyError(item)

        switched = switch.getValue() if switch else 0

        relay.setValue(value ^ switched)
