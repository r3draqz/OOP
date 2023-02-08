import random

class insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def lenflight(self):
        self.flight = random.randint(1, 10)

    def get_lenflight(self):
        return self.flight