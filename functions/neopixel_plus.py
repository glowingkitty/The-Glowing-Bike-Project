import random
import time

from colr import color


class NeoPixel:
    def __init__(self, pin, n, bpp=3, brightness=1.0, auto_write=True, pixel_order=None, test=False):
        self.strip_length = n
        self.test = test
        if self.test:
            self.leds = [[0, 0, 0] for x in range(self.strip_length)]
        else:
            from neopixel import NeoPixel
            from machine import Pin
            self.leds = NeoPixel(
                pin=Pin(pin, Pin.OUT),
                n=self.strip_length,
                bpp=bpp,
                brightness=brightness,
                auto_write=auto_write,
                pixel_order=pixel_order)

    def write(self):
        if self.test:
            print(
                ''.join(color('  ', back=(x[0], x[1], x[2])) for x in self.leds))

        else:
            self.leds.write()

    def random_flashing(self):
        while True:
            self.leds = [
                (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255)) for x in range(self.strip_length)]
            self.write()
