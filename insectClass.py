import random

class insect:

    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0

    def lenflight(self):
        self.flight = random.randint(1, 10)

    def get_miles(self):
        return self.flight

    def get_name(self):
        return self.name