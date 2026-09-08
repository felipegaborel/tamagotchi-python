from .animal import Animal


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def brincar(self):
        # Use base behavior and add a small bonus
        super().brincar()
        self.happiness = min(100, self.happiness + 5)
        self._sync_attributes()
