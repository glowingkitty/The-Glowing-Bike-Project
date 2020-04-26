
class DrivingAnimation():
    def __init__(self, bike):
        self.bike = bike

        # make top leds of self.leds_front white and back leds of self.leds_front red
        if self.bike.test:
            for i in range(len(self.bike.leds_front.leds)):
                color = (255*self.bike.animation_brightness, 255*self.bike.animation_brightness, 255*self.bike.animation_brightness) if i > (
                    len(self.bike.leds_front.leds)/2) else (255*self.bike.animation_brightness, 0, 0)
                self.bike.leds_front.leds[i] = color
        else:
            for i in range(len(self.bike.leds_front)):
                color = (255*self.bike.animation_brightness, 255*self.bike.animation_brightness, 255*self.bike.animation_brightness) if i > (
                    len(self.bike.leds_front.leds)/2) else (255*self.bike.animation_brightness, 0, 0)
                self.bike.leds_front[i] = color

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
