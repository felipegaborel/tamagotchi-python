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
        preenchido = int(valor / 5)
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

    def alimentar(self):
        self.fome = max(0, self.fome - 20)
        self.energia = min(100, self.energia + 10)
        print(f"\n🍖 {self.nome} foi alimentado!")

    def brincar(self):
        self.felicidade = min(100, self.felicidade + 15)
        self.energia = max(0, self.energia - 10)
        self.fome = min(100, self.fome + 10)
        print(f"\n🎾 {self.nome} brincou bastante!")

    def dormir(self):
        self.energia = min(100, self.energia + 30)
        self.fome = min(100, self.fome + 15)
        print(f"\n😴 {self.nome} descansou!")

    def banho(self):
        self.felicidade = min(100, self.felicidade + 5)
        print(f"\n🚿 {self.nome} tomou banho!")

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
        print("\n" + "=" * 50)
        print(f"🐶 {self.nome}")
        print()
        print(f"❤️ Saúde      {self.barra(self.saude)} {self.saude}")
        print(f"⚡ Energia    {self.barra(self.energia)} {self.energia}")
        print(f"🍖 Fome       {self.barra(self.fome)} {self.fome}")
        print(f"😊 Felicidade {self.barra(self.felicidade)} {self.felicidade}")
        print("=" * 50)
