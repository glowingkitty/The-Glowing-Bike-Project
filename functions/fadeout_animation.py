class FadeOutAnimation():
    def __init__(self, bike, led_strip):
        self.bike = bike

        if led_strip == 'right':
            selected_leds = self.bike.leds_right.leds if self.bike.test else self.bike.leds_right
        elif led_strip == 'left':
            selected_leds = self.bike.leds_left.leds if self.bike.test else self.bike.leds_left
        elif led_strip == 'front':
            selected_leds = self.bike.leds_front.leds if self.bike.test else self.bike.leds_front

        for i in range(len(selected_leds)):
            color = (0, 0, 0)
            if self.bike.test:
                if led_strip == 'right':
                    self.bike.leds_right.leds[i] = color
                elif led_strip == 'left':
                    self.bike.leds_left.leds[i] = color
                elif led_strip == 'front':
                    self.bike.leds_front.leds[i] = color
            else:
                if led_strip == 'right':
                    self.bike.leds_right[i] = color
                elif led_strip == 'left':
                    self.bike.leds_left[i] = color
                elif led_strip == 'front':
                    self.bike.leds_front[i] = color
