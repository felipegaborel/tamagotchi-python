from animal import Animal
from menu import Menu


class Game:
    def __init__(self):
        self.animal = Animal("Mochi")
        self.menu = Menu()

    def run(self):
        while True:
            self.menu.show_main_menu()
            choice = self.menu.get_choice()

            if choice == "1":
                self.animal.feed()
                print("You fed your pet.")
            elif choice == "2":
                self.animal.play()
                print("You played with your pet.")
            elif choice == "3":
                self.animal.sleep()
                print("Your pet is resting.")
            elif choice == "4":
                print(self.animal.status())
            elif choice == "5":
                print("Bye!")
                break
            else:
                print("Invalid option.")
