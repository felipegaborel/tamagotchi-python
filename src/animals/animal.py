class Animal:
    def __init__(self, name: str):
        self.name = name
        self.nome = name
        self.idade = 0
        self.hunger = 5
        self.fome = self.hunger
        self.happiness = 5
        self.felicidade = self.happiness
        self.energy = 5
        self.energia = self.energy
        self.saude = 10
        self.esta_vivo = True

    def _sync_attributes(self):
        self.nome = self.name
        self.fome = self.hunger
        self.felicidade = self.happiness
        self.energia = self.energy

    def barra(self, valor):
        total = 20
        preenchido = int((valor / 100) * total)
        vazio = total - preenchido
        return "█" * preenchido + "░" * vazio

    def feed(self):
        self.hunger = min(10, self.hunger + 1)
        self._sync_attributes()

    def play(self):
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)
        self._sync_attributes()

    def sleep(self):
        self.energy = min(10, self.energy + 1)
        self._sync_attributes()

    def status(self):
        self._sync_attributes()
        return {
            "name": self.name,
            "nome": self.nome,
            "idade": self.idade,
            "hunger": self.hunger,
            "fome": self.fome,
            "happiness": self.happiness,
            "felicidade": self.felicidade,
            "energy": self.energy,
            "energia": self.energia,
            "saude": self.saude,
            "esta_vivo": self.esta_vivo,
        }

    def mostrar_status(self):
        print("Energia :", self.barra(self.energia), self.energia)
        print("Fome    :", self.barra(self.fome), self.fome)
        print("Saúde   :", self.barra(self.saude), self.saude)
        print("Felicidade:", self.barra(self.felicidade), self.felicidade)
