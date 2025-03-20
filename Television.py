class Television:
    def __init__(self, power_button):
        self.channel = 3
        self.volume = 5

    def channel_up(self):
        self.channel += 1

    def return_channel(self):
        return self.channel

    def channel_down(self):
        self.channel -= 1

    def volume_up(self):
        self.volume += 1

    def volume_up(self):
        self.volume -= 1

    def get_volume(self):
        return self.channel