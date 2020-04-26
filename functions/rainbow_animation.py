import math


class RainbowAnimation():
    def __init__(self, bike):
        self.bike = bike

        # turn LEDs rainbow
        self.bike.time_passed += 0.06
        if self.bike.test:
            for i in range(len(self.bike.leds_front.leds)):
                color = self.rainbow(self.bike.time_passed, i,
                                     self.bike.animation_brightness)
                self.bike.leds_front.leds[i] = color
        else:
            for i in range(len(self.bike.leds_front)):
                color = self.rainbow(self.bike.time_passed, i,
                                     self.bike.animation_brightness)
                self.bike.leds_front[i] = color

        if self.bike.animation_up_and_down:
            self.bike.animation_brightness, self.bike.animation_direction = self.change_brightness(
                self.bike.animation_brightness, self.bike.animation_direction)

    def rainbow(self, t, i, brightness):
        a = (0.5, 0.5, 0.5)
        b = (0.5, 0.5, 0.5)
        c = (1.0, 1.0, 1.0)
        d = (0.00, 0.33, 0.67)

        k = t + 0.05 * i

        r = a[0] + b[0] * math.cos(6.28318 * (c[0] * k + d[0]))
        g = a[1] + b[1] * math.cos(6.28318 * (c[1] * k + d[1]))
        b = a[2] + b[2] * math.cos(6.28318 * (c[2] * k + d[2]))

        return (int(255.0 * r * brightness), int(255.0 * g * brightness), int(255.0 * b * brightness))

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
