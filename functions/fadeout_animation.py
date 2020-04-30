class FadeOutAnimation():
    def __init__(self, bike, led_strip):
        self.bike = bike

        if led_strip == 'front':
            selected_leds = self.bike.leds_front
        elif led_strip == 'center':
            selected_leds = self.bike.leds_center
        elif led_strip == 'back':
            selected_leds = self.bike.leds_back

        for i in range(selected_leds.strip_length):
            color = (0, 0, 0)
            if led_strip == 'front':
                self.bike.leds_front.leds[i] = color
            elif led_strip == 'center':
                self.bike.leds_center.leds[i] = color
            elif led_strip == 'back':
                self.bike.leds_back.leds[i] = color
