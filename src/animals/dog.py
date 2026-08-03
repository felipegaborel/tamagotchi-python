from .animal import Animal


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def brincar(self):
        super().brincar()
        self.felicidade = min(100, self.felicidade + 5)
