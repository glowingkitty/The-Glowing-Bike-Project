
class DrivingAnimation():
    def __init__(self, bike):
        self.bike = bike

        # make top leds of self.leds_center white and back leds of self.leds_center red
        # make front leds white
        for i in range(self.bike.leds_front.strip_length):
            i = self.bike.leds_front.get_led(i)
            self.bike.leds_front.leds[i] = (255, 255, 255)

        # make center leds red and white
        for i in range(self.bike.leds_center.strip_length):
            i = self.bike.leds_center.get_led(i)
            color = (round(255*self.bike.animation_brightness), round(255*self.bike.animation_brightness), round(255*self.bike.animation_brightness)) if i > (
                round(self.bike.leds_center.strip_length/2)) else (round(255*self.bike.animation_brightness), 0, 0)
            self.bike.leds_center.leds[i] = color

        # make back part of back leds red up
        for i in range(self.bike.leds_back.strip_length):
            if i < round(self.bike.leds_back.strip_length/2)-6 or i > round(self.bike.leds_back.strip_length/2)+5:
                color = (0, 0, 0)
            else:
                color = (255, 0, 0)
            i = self.bike.leds_back.get_led(i)
            self.bike.leds_back.leds[i] = color

        if self.bike.animation_up_and_down:
            self.bike.animation_brightness, self.bike.animation_direction = self.change_brightness(
                self.bike.animation_brightness, self.bike.animation_direction)

    def change_brightness(self, brightness, direction):
        if direction == 'up':
            brightness = brightness + 0.025
        else:
            brightness = brightness - 0.025

        if brightness <= 0.5:
            direction = 'up'
        elif brightness >= 0.7:
            direction = 'down'

        return brightness, direction
