import random
import time

import keyboard
from neopixel_plus import NeoPixel

from functions.driving_animation import DrivingAnimation
from functions.fadeout_animation import FadeOutAnimation
from functions.turn_animation import TurnAnimation


class Bike():
    def __init__(self, test=False):
        self.leds_front = NeoPixel(pin=5, n=30, bpp=3, test=test)
        self.leds_left = NeoPixel(pin=17, n=5, bpp=3, test=test)
        self.leds_right = NeoPixel(pin=18, n=5, bpp=3, test=test)
        self.mode = 'relaxed'
        self.time_passed = 0
        self.animation_brightness = 0.0
        self.animation_direction = 'up'
        self.animation_up_and_down = True

        self.switch_right_value = 0
        self.switch_left_value = 0

        self.test = test

    def start_driving(self):
        while True:
            # check if mode has changed
            self.switches = {
                'left': self.switch_left,
                'right': self.switch_right
            }

            if self.switches['left'] == True and self.switches['right'] == True:
                self.mode = 'relaxed'
                self.fade_out('left')
                self.fade_out('right')
                self.rainbow_animation()

            elif self.switches['left'] == False and self.switches['right'] == False:
                self.mode = 'safe'
                self.fade_out('left')
                self.fade_out('right')
                self.driving_animation()

            elif self.switches['left'] == True:
                self.mode = 'turn_left'
                self.fade_out('front')
                self.fade_out('right')
                self.turn_left()

            elif self.switches['right'] == True:
                self.mode = 'turn_right'
                self.fade_out('front')
                self.fade_out('left')
                self.turn_right()

            # show status of switches
            print('Switch left: {}'.format(self.switches['left']))
            print('Switch right: {}'.format(self.switches['right']))
            print()
            self.leds_left.write()
            print()
            self.leds_front.write()
            print()
            self.leds_right.write()
            print()
            print()

    @property
    def switch_left(self):
        if self.test:
            # check if keyboard right was pressed
            if keyboard.is_pressed('left'):
                if self.switch_left_value == 0:
                    self.switch_left_value = 1
                else:
                    self.switch_left_value = 0

            return self.switch_left_value
        else:
            from machine import Pin
            return Pin(10, Pin.OUT)

    @property
    def switch_right(self):
        if self.test:
            # check if keyboard right was pressed
            if keyboard.is_pressed('right'):
                if self.switch_right_value == 0:
                    self.switch_right_value = 1
                else:
                    self.switch_right_value = 0

            return self.switch_right_value
        else:
            from machine import Pin
            return Pin(11, Pin.OUT)

    def turn_right(self):
        self = TurnAnimation(bike=self, direction='right').bike

    def turn_left(self):
        self = TurnAnimation(bike=self, direction='left').bike

    def rainbow_animation(self):
        # relaxed mode
        self.leds_front.rainbow_animation(loop=False)

    def driving_animation(self):
        # safe mode
        self = DrivingAnimation(bike=self).bike

    def fade_out(self, led_strip):
        self = FadeOutAnimation(bike=self, led_strip=led_strip).bike


Bike(test=True).start_driving()
