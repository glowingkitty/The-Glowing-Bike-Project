
class TurnAnimation():
    def __init__(self, bike, direction):
        # turn LEDs red
        self.bike = bike

        if direction == 'right':
            selected_leds = self.bike.leds_right.leds if self.bike.test else self.bike.leds_right
        elif direction == 'left':
            selected_leds = self.bike.leds_left.leds if self.bike.test else self.bike.leds_left

        for i in range(len(selected_leds)):
            color = (255*self.bike.animation_brightness, 0, 0)
            if self.bike.test:
                if direction == 'right':
                    self.bike.leds_right.leds[i] = color
                elif direction == 'left':
                    self.bike.leds_left.leds[i] = color
            else:
                if direction == 'right':
                    self.bike.leds_right[i] = color
                elif direction == 'left':
                    self.bike.leds_left[i] = color

        if self.bike.animation_up_and_down:
            self.bike.animation_brightness, self.bike.animation_direction = self.change_brightness(
                self.bike.animation_brightness, self.bike.animation_direction)

    def change_brightness(self, brightness, direction):
        if direction == 'up':
            brightness = brightness + 0.025
        else:
            brightness = brightness - 0.025

        if brightness <= 0.1:
            direction = 'up'
        elif brightness >= 0.7:
            direction = 'down'

        return brightness, direction
