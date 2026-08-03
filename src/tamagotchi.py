class Tamagotchi:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5

    def feed(self):
        self.hunger += 1

    def play(self):
        self.happiness += 1
        self.energy -= 1
