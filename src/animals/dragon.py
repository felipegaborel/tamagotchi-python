from .animal import Animal

# Nota: subclasses agora usam os atributos canônicos (english) e chamam _sync_attributes()
# para manter compatibilidade com código que espera aliases em português.

class Dragon(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def brincar(self):
        # Dragons consume more energy when playing
        super().brincar()
        self.energy = max(0, self.energy - 15)
        self._sync_attributes()
