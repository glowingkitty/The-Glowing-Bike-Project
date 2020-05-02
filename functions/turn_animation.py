
class TurnAnimation():
    def __init__(self, bike, direction):
        self.bike = bike
        self.direction = direction

        self.leds_front()
        self.leds_center()
        self.leds_back()

    def leds_front(self):
        # make front LEDs glow up white in direction

        # make all dark
        for i in range(self.bike.leds_front.strip_length):
            self.bike.leds_front.leds[i] = (0, 0, 0)

        # make leds turning right or left glow
        led_front_middle = round(self.bike.leds_front.strip_length/2)
        if self.direction == 'right':
            for i in range(self.bike.leds_front.lastlightup):
                led_num = self.bike.leds_front.get_led(led_front_middle+i)
                self.bike.leds_front.leds[led_num] = (255, 255, 255)

        elif self.direction == 'left':
            for i in range(self.bike.leds_front.lastlightup):
                led_num = self.bike.leds_front.get_led(led_front_middle-i)
                self.bike.leds_front.leds[led_num] = (255, 255, 255)

        if led_front_middle + self.bike.leds_front.lastlightup == self.bike.leds_front.strip_length:
            self.bike.leds_front.glow_direction = 'down'
        elif self.bike.leds_front.lastlightup == 0:
            self.bike.leds_front.glow_direction = 'up'

        if self.bike.leds_front.glow_direction == 'up':
            self.bike.leds_front.lastlightup += 1
        else:
            self.bike.leds_front.lastlightup -= 1

        # make led in the middle glow
        led_num = self.bike.leds_front.get_led(led_front_middle)
        self.bike.leds_front.leds[led_num] = (255, 255, 255)

    def leds_center(self):
        # make center LEDs dark
        for i in range(self.bike.leds_center.strip_length):
            self.bike.leds_center.leds[i] = (0, 0, 0)

    def leds_back(self):
        # make all dark
        for i in range(self.bike.leds_back.strip_length):
            self.bike.leds_back.leds[i] = (0, 0, 0)

        # make leds turning right or left glow
        led_back_middle = round(self.bike.leds_back.strip_length/2)
        if self.direction == 'right':
            for i in range(self.bike.leds_back.lastlightup):
                led_num = self.bike.leds_back.get_led(led_back_middle+i+5)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5:
                    self.bike.leds_back.leds[led_num] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+1:
                    self.bike.leds_back.leds[led_num+1] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+2:
                    self.bike.leds_back.leds[led_num+2] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+3:
                    self.bike.leds_back.leds[led_num+3] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+4:
                    self.bike.leds_back.leds[led_num+4] = (255, 0, 0)

        elif self.direction == 'left':
            for i in range(self.bike.leds_back.lastlightup):
                led_num = self.bike.leds_back.get_led(led_back_middle-i-6)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5:
                    self.bike.leds_back.leds[led_num] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+1:
                    self.bike.leds_back.leds[led_num-1] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+2:
                    self.bike.leds_back.leds[led_num-2] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+3:
                    self.bike.leds_back.leds[led_num-3] = (255, 0, 0)
                if self.bike.leds_back.strip_length >= led_back_middle+i+5+4:
                    self.bike.leds_back.leds[led_num-4] = (255, 0, 0)

        if led_back_middle+5 + self.bike.leds_back.lastlightup >= self.bike.leds_back.strip_length-2:
            self.bike.leds_back.glow_direction = 'down'
        elif self.bike.leds_back.lastlightup == 0:
            self.bike.leds_back.glow_direction = 'up'

        if self.bike.leds_back.glow_direction == 'up':
            self.bike.leds_back.lastlightup += 5
        else:
            self.bike.leds_back.lastlightup -= 5

        # make led in the middle glow
        led_num = self.bike.leds_back.get_led(led_back_middle)
        self.bike.leds_back.leds[led_num] = (255, 0, 0)
        self.bike.leds_back.leds[led_num+1] = (255, 0, 0)
        self.bike.leds_back.leds[led_num+2] = (255, 0, 0)
        self.bike.leds_back.leds[led_num+3] = (255, 0, 0)
        self.bike.leds_back.leds[led_num+4] = (255, 0, 0)
        self.bike.leds_back.leds[led_num+5] = (255, 0, 0)
        self.bike.leds_back.leds[led_num-1] = (255, 0, 0)
        self.bike.leds_back.leds[led_num-2] = (255, 0, 0)
        self.bike.leds_back.leds[led_num-3] = (255, 0, 0)
        self.bike.leds_back.leds[led_num-4] = (255, 0, 0)
        self.bike.leds_back.leds[led_num-5] = (255, 0, 0)
        self.bike.leds_back.leds[led_num-6] = (255, 0, 0)
