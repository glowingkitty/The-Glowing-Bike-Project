import random
import time

from colr import color


class TestLEDs():
    def __init__(self, strip_length):
        self.strip_length = strip_length
        self.leds = [[0, 0, 0] for x in range(self.strip_length)]

    def write(self):
        print(
            ''.join(color('  ', back=(x[0], x[1], x[2])) for x in self.leds))

    def random_flashing(self):
        while True:
            self.leds = [
                (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)) for x in range(self.strip_length)]
            self.write()
