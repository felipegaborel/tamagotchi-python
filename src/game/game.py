import random

from animals.animal import Animal
from game.actions import Actions
from game.events import Events
from ui.menu import Menu


class Game:
    def __init__(self):
        self.animal = Animal("Mochi")
        self.actions = Actions(self.animal)
        self.events = Events(self.animal)
        self.menu = Menu()
        self.velocidade = 1

    def _apply_turn_decay(self):
        self.animal.energy = max(0, self.animal.energy - self.velocidade)
        self.animal.hunger = min(10, self.animal.hunger + self.velocidade)
        self.animal.idade += 1
        self.animal.happiness = max(0, self.animal.happiness - self.velocidade)
        self.animal._sync_attributes()

    def _trigger_random_event(self):
        chance = random.randint(1, 10)
        if chance == 1:
            print(self.events.pet_encontrou_comida())
        elif chance == 2:
            print(self.events.pet_ficou_doente())
        elif chance == 3:
            print(self.events.pet_encontrou_brinquedo())

    def run(self):
        print("Digite o nome do seu pet")
        nome = input(">> ").strip()
        if not nome:
            nome = "Mochi"

        self.animal = Animal(nome)
        self.actions = Actions(self.animal)
        self.events = Events(self.animal)

        print("Escolha a dificuldade")
        print("1 - Fácil")
        print("2 - Normal")
        print("3 - Difícil")

        nivel = input(">> ")

        if nivel == "1":
            self.velocidade = 1
        elif nivel == "2":
            self.velocidade = 2
        else:
            self.velocidade = 3

        while True:
            self._apply_turn_decay()
            self._trigger_random_event()
            self.menu.show_main_menu()
            choice = self.menu.get_choice()

            if choice == "1":
                print(self.actions.alimentar())
            elif choice == "2":
                print(self.actions.brincar())
            elif choice == "3":
                print(self.actions.dormir())
            elif choice == "4":
                print(self.actions.dar_banho())
            elif choice == "5":
                print(self.actions.curar())
            elif choice == "6":
                self.menu.mostrar_status(self.animal)
            elif choice == "7":
                print("Bye!")
                break
            else:
                print("Invalid option.")
