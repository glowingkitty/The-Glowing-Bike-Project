
class DrivingAnimation():
    def __init__(self, bike):
        self.bike = bike

        # make top leds of self.leds_center white and back leds of self.leds_center red
        # make front leds white
        for i in range(self.bike.leds_front.strip_length):
            self.bike.leds_front.leds[i] = (255, 255, 255)

        # make center leds red and white
        for i in range(self.bike.leds_center.strip_length):
            color = (round(255*self.bike.animation_brightness), round(255*self.bike.animation_brightness), round(255*self.bike.animation_brightness)) if i > (
                round(self.bike.leds_center.strip_length/2)) else (round(255*self.bike.animation_brightness), 0, 0)
            self.bike.leds_center.leds[i] = color

        # make back leds red
        for i in range(self.bike.leds_back.strip_length):
            self.bike.leds_back.leds[i] = (255, 0, 0)

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
