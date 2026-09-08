from .animal import Animal


class Dragon(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def brincar(self):
        # Dragons consume more energy when playing
        super().brincar()
        self.energy = max(0, self.energy - 15)
        self._sync_attributes()
