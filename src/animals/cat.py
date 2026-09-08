from .animal import Animal


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def dormir(self):
        # Base sleep behavior and extra energy recovery for cats
        super().dormir()
        self.energy = min(100, self.energy + 10)
        self._sync_attributes()
