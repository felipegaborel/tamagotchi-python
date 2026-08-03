class Menu:
    def show_main_menu(self):
        print("\n=== Tamagotchi Menu ===")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Status")
        print("5. Exit")

    def get_choice(self):
        return input("Choose an option: ").strip()
