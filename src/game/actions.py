from game.level import LevelSystem


class Actions:
    def __init__(self, animal):
        self.animal = animal

    def alimentar(self):
        self.animal.feed()
        LevelSystem.ganhar_xp(self.animal, 5)
        return self.animal.status()

    def brincar(self):
        self.animal.play()
        LevelSystem.ganhar_xp(self.animal, 10)
        return self.animal.status()

    def dormir(self):
        self.animal.sleep()
        LevelSystem.ganhar_xp(self.animal, 3)
        return self.animal.status()

    def dar_banho(self):
        self.animal.saude = min(10, self.animal.saude + 1)
        self.animal.esta_vivo = True
        LevelSystem.ganhar_xp(self.animal, 2)
        return self.animal.status()

    def curar(self):
        self.animal.saude = min(10, self.animal.saude + 2)
        self.animal.esta_vivo = True
        return self.animal.status()
