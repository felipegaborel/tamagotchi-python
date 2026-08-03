class Actions:
    def __init__(self, animal):
        self.animal = animal

    def alimentar(self):
        self.animal.feed()
        return self.animal.status()

    def brincar(self):
        self.animal.play()
        return self.animal.status()

    def dormir(self):
        self.animal.sleep()
        return self.animal.status()

    def dar_banho(self):
        self.animal.saude = min(10, self.animal.saude + 1)
        self.animal.esta_vivo = True
        return self.animal.status()

    def curar(self):
        self.animal.saude = min(10, self.animal.saude + 2)
        self.animal.esta_vivo = True
        return self.animal.status()
