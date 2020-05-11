import random
import time

from neopixel_plus import NeoPixel

from glowingbike.functions.driving_animation import DrivingAnimation
from glowingbike.functions.fadeout_animation import FadeOutAnimation
from glowingbike.functions.turn_animation import TurnAnimation


class Bike():
    def __init__(self,
                 leds_front_pin=13,
                 leds_front_length=9,
                 leds_front_start_point=0,
                 leds_center_pin=12,
                 leds_center_length=60,
                 leds_center_start_point=0,
                 leds_back_pin=14,
                 leds_back_length=58,
                 leds_back_start_point=-4,
                 switch_left_pin=3,
                 switch_right_pin=1,
                 test=False
                 ):
        # setting up the LEDs
        self.leds_front = NeoPixel(
            pin_num=leds_front_pin, n=leds_front_length, start_point=leds_front_start_point, brightness=1, bpp=3, test=test) if leds_front_pin and leds_front_length else None
        self.leds_center = NeoPixel(
            pin_num=leds_center_pin, n=leds_center_length, start_point=leds_center_start_point, bpp=3, test=test) if leds_center_pin and leds_center_length else None
        self.leds_back = NeoPixel(
            pin_num=leds_back_pin, n=leds_back_length, start_point=leds_back_start_point, brightness=1, bpp=3, test=test) if leds_back_pin and leds_back_length else None
        self.mode = 'relaxed'
        self.time_passed = 0
        self.animation_brightness = 0.0
        self.animation_direction = 'up'
        self.animation_up_and_down = True

        # setting up the switches
        self.switch_left_pin = switch_left_pin
        self.switch_right_pin = switch_right_pin
        self.switch_right_value = 0
        self.switch_left_value = 0

        self.test = test

    def on(self):
        while True:
            # check if mode has changed
            self.switches = {
                'left': self.switch_left,
                'right': self.switch_right
            }

            if type(self.switches['right']) == int and type(self.switches['left']) == int:
                # dual switch mode
                if self.switches['left'] == 1 and self.switches['right'] == 1:
                    self.mode = 'relaxed'
                    self.rainbow_animation()

                elif self.switches['left'] == 0 and self.switches['right'] == 0:
                    self.mode = 'safe'
                    self.driving_animation()

                elif self.mode == 'turn_left' or (self.mode == 'safe' and self.switches['left'] == 1) or (self.mode == 'relaxed' and self.switches['left'] == 0):
                    self.mode = 'turn_left'
                    self.turn_left()

                elif self.mode == 'turn_right' or (self.mode == 'safe' and self.switches['right'] == 1) or (self.mode == 'relaxed' and self.switches['right'] == 0):
                    self.mode = 'turn_right'
                    self.turn_right()

            else:
                # single switch mode
                if self.switches['right'] == True:
                    self.mode = 'relaxed'
                    self.rainbow_animation()

                else:
                    self.mode = 'safe'
                    self.driving_animation()

            # show status of switches
            print('Switch left: {}'.format(self.switches['left']))
            print('Switch right: {}'.format(self.switches['right']))
            print()
            if self.leds_front:
                self.leds_front.write()
                print()
            if self.leds_center:
                self.leds_center.write()
                print()
            if self.leds_back:
                self.leds_back.write()
                print()
            print()

    def restart(self):
        if self.test:
            print('Restart can only be performed on real hardware, not in test mode.')
        else:
            import machine
            machine.reset()

    @property
    def switch_left(self):
        if not self.switch_left_pin:
            return None

        if self.test:
            import keyboard
            # check if keyboard right was pressed
            if keyboard.is_pressed('left'):
                if self.switch_left_value == 0:
                    self.switch_left_value = 1
                else:
                    self.switch_left_value = 0

            return self.switch_left_value
        else:
            from machine import Pin
            # TODO pin value not working
            return Pin(self.switch_left_pin, Pin.IN).value()

    @property
    def switch_right(self):
        if not self.switch_right_pin:
            return None

        if self.test:
            import keyboard
            # check if keyboard right was pressed
            if keyboard.is_pressed('right'):
                if self.switch_right_value == 0:
                    self.switch_right_value = 1
                else:
                    self.switch_right_value = 0

            return self.switch_right_value
        else:
            from machine import Pin
            return Pin(self.switch_right_pin, Pin.IN).value()

    def turn_right(self):
        print('turn_right')
        self = TurnAnimation(bike=self, direction='right').bike

    def turn_left(self):
        print('turn_left')
        self = TurnAnimation(bike=self, direction='left').bike

    def rainbow_animation(self):
        # relaxed mode
        self.leds_front.rainbow_animation(limit=1)
        self.leds_center.rainbow_animation(limit=1)
        self.leds_back.rainbow_animation(limit=1)

    def driving_animation(self):
        # safe mode
        self = DrivingAnimation(bike=self).bike

    def fade_out(self, led_strip):
        self = FadeOutAnimation(bike=self, led_strip=led_strip).bike
