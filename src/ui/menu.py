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
        print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
        print(f"{Colors.YELLOW}Nome:{Colors.RESET} {animal.nome}")
        print(f"{Colors.RED}❤️ Saúde:{Colors.RESET} {animal.barra(animal.saude)} {animal.saude}")
        print(f"{Colors.GREEN}🍖 Fome:{Colors.RESET} {animal.barra(animal.fome)} {animal.fome}")
        print(f"{Colors.BLUE}⚡ Energia:{Colors.RESET} {animal.barra(animal.energia)} {animal.energia}")
        print(f"{Colors.MAGENTA}😊 Felicidade:{Colors.RESET} {animal.barra(animal.felicidade)} {animal.felicidade}")
        print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")

    def get_choice(self):
        return input(f"{Colors.YELLOW}Choose an option: {Colors.RESET}").strip()
