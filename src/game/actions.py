from game.level import LevelSystem

# Alterações:
# - Actions agora usa a API do Animal (feed/play/sleep/bath) ao invés de manipular atributos 'saude', 'fome' diretamente.
# - Isso garante que a lógica de sincronização e limites esteja centralizada em Animal.

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
        # Use the Animal API rather than direct attribute manipulation
        self.animal.bath()
        # Ensure alive flag is set
        self.animal.alive = True
        self.animal._sync_attributes()
        LevelSystem.ganhar_xp(self.animal, 2)
        return self.animal.status()

    def curar(self):
        # Heal the animal
        self.animal.health = min(100, self.animal.health + 20)
        self.animal.alive = True
        self.animal._sync_attributes()
        return self.animal.status()
