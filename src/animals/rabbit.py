from .animal import Animal


class Rabbit(Animal):
    def __init__(self, name: str):
        super().__init__(name)
