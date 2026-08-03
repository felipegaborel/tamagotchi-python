from .animal import Animal


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def dormir(self):
        super().dormir()
        self.energia = min(100, self.energia + 10)
