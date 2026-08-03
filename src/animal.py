class Animal:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5

    def feed(self):
        self.hunger = min(10, self.hunger + 1)

    def play(self):
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)

    def sleep(self):
        self.energy = min(10, self.energy + 1)

    def status(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy,
        }
