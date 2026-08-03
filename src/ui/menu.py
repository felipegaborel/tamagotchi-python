from ui.colors import Colors


class Menu:
    def show_main_menu(self):
        print(f"\n{Colors.CYAN}=== Tamagotchi Menu ==={Colors.RESET}")
        print(f"{Colors.GREEN}1. Alimentar{Colors.RESET}")
        print(f"{Colors.GREEN}2. Brincar{Colors.RESET}")
        print(f"{Colors.GREEN}3. Dormir{Colors.RESET}")
        print(f"{Colors.GREEN}4. Dar banho{Colors.RESET}")
        print(f"{Colors.GREEN}5. Curar{Colors.RESET}")
        print(f"{Colors.GREEN}6. Status{Colors.RESET}")
        print(f"{Colors.GREEN}7. Exit{Colors.RESET}")

    def mostrar_status(self, animal):
        print("=" * 40)
        print("Nome:", animal.nome)
        print("❤️ Saúde:", animal.saude)
        print("🍖 Fome:", animal.fome)
        print("⚡ Energia:", animal.energia)
        print("😊 Felicidade:", animal.felicidade)
        print("=" * 40)

    def get_choice(self):
        return input(f"{Colors.YELLOW}Choose an option: {Colors.RESET}").strip()
