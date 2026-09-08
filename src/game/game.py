import random

from animals.animal import Animal
from game.actions import Actions
from game.events import Events
from ui.menu import Menu

# Alterações realizadas (comentário):
# - Centralizei a verificação de vida em verificar_vida() e removi código aninhado incorreto.
# - Usei atributos canônicos (health, hunger, energy, happiness, age) para facilitar manutenção.
# - Mantive chamadas para _sync_attributes() para compatibilidade com aliases PT-BR.

class Game:
    def __init__(self):
        self.animal = Animal("Mochi")
        self.actions = Actions(self.animal)
        self.events = Events(self.animal)
        self.menu = Menu()
        self.velocidade = 1

    def verificar_vida(self) -> bool:
        """Verifica se o pet ainda está vivo; retorna False se morto."""
        if self.animal.health <= 0:
            self.animal.alive = False
            # sincroniza aliases
            if hasattr(self.animal, "_sync_attributes"):
                self.animal._sync_attributes()
            print("\n💀 Seu pet morreu.")
            print("Obrigado por jogar.")
            return False
        return True

    def _apply_turn_decay(self):
        # Aplica decaimento por turno usando atributos canônicos (inglês)
        self.animal.energy = max(0, self.animal.energy - self.velocidade)
        self.animal.hunger = min(100, self.animal.hunger + self.velocidade)
        self.animal.age += 1
        self.animal.happiness = max(0, self.animal.happiness - self.velocidade)

        # efeitos por condições
        if self.animal.hunger >= 90:
            self.animal.health = max(0, self.animal.health - 10)
        if self.animal.energy <= 10:
            self.animal.health = max(0, self.animal.health - 5)

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

            # checa se o pet ainda vive antes de seguir
            if not self.verificar_vida():
                break

            self._trigger_random_event()
            self.menu.show_main_menu()
            choice = self.menu.get_choice(timeout=60)

            # Se houve timeout de inatividade, mata o pet
            if choice is None:
                print("\nVocê ficou inativo por muito tempo... seu pet não sobreviveu à inatividade.")
                self.animal.health = 0
                if hasattr(self.animal, "_sync_attributes"):
                    self.animal._sync_attributes()
                # chamar verificar_vida para exibir mensagem e encerrar
                self.verificar_vida()
                break

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
                print("Opção inválida.")
