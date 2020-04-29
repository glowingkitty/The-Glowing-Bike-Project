
class TurnAnimation():
    def __init__(self, bike, direction):
        # turn LEDs red
        self.bike = bike

        for i in range(len(self.bike.leds_center.leds)):
            color = (255*self.bike.animation_brightness, 0, 0)
            if direction == 'right':
                # make leds right red, left dark
                if i >= len(self.bike.leds_center.leds)/2:
                    self.bike.leds_center.leds[i] = (255, 0, 0)
                else:
                    self.bike.leds_center.leds[i] = (0, 0, 0)

            elif direction == 'left':
                if i <= len(self.bike.leds_center.leds)/2:
                    self.bike.leds_center.leds[i] = (255, 0, 0)
                else:
                    self.bike.leds_center.leds[i] = (0, 0, 0)

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
