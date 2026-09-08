import os
import sys
import time

from ui.colors import Colors


# Alterações:
# - Unifiquei a exibição de status para usar a API do Animal (status_bar) e atributos canônicos.
# - Adicionado `timed_input` para detectar inatividade do usuário e retornar None em timeout.
# - Funções utilitárias continuam em português para melhor UX do usuário brasileiro.


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def timed_input(prompt: str, timeout: int = 60):
    """Cross-platform timed input. Retorna a string do usuário ou None se timeout."""
    # Windows implementation
    if os.name == "nt":
        import msvcrt

        sys.stdout.write(prompt)
        sys.stdout.flush()
        start = time.time()
        input_str = ""
        while True:
            if msvcrt.kbhit():
                ch = msvcrt.getwche()
                if ch in ("\r", "\n"):
                    print("")
                    return input_str
                if ch == "\b":
                    input_str = input_str[:-1]
                    sys.stdout.write('\b \b')
                else:
                    input_str += ch
            if (time.time() - start) > timeout:
                print("")
                return None
            time.sleep(0.05)

    # POSIX implementation (select)
    else:
        import select

        sys.stdout.write(prompt)
        sys.stdout.flush()
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            return sys.stdin.readline().rstrip("\n")
        else:
            print("")
            return None


def mostrar_menu(timeout: int = 60):

    print("=" * 50)
    print("🐾 TAMAGOTCHI PYTHON 🐾")
    print("=" * 50)

    print("\n1 🍖 Alimentar")
    print("2 🎾 Brincar")
    print("3 😴 Dormir")
    print("4 🚿 Dar banho")
    print("5 📊 Mostrar Status")
    print("6 🚪 Sair")

    print("\n" + "=" * 50)

    # Retorna None se houve inatividade
    return timed_input("Escolha uma opção: ", timeout=timeout)


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
        # Ensure attributes are synced and use the status_bar helper
        if hasattr(animal, "_sync_attributes"):
            animal._sync_attributes()

        print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
        print(f"{Colors.YELLOW}Nome:{Colors.RESET} {animal.nome}")
        print(f"{Colors.RED}❤️ Saúde:{Colors.RESET} {animal.status_bar(animal.health)} {animal.health}")
        print(f"{Colors.GREEN}🍖 Fome:{Colors.RESET} {animal.status_bar(animal.hunger)} {animal.hunger}")
        print(f"{Colors.BLUE}⚡ Energia:{Colors.RESET} {animal.status_bar(animal.energy)} {animal.energy}")
        print(f"{Colors.MAGENTA}😊 Felicidade:{Colors.RESET} {animal.status_bar(animal.happiness)} {animal.happiness}")
        print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")

    def get_choice(self, timeout: int = 60):
        # Returns None if timeout
        return timed_input(f"{Colors.YELLOW}Escolha uma opção: {Colors.RESET}", timeout=timeout)
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
        # Ensure attributes are synced and use the status_bar helper
        if hasattr(animal, "_sync_attributes"):
            animal._sync_attributes()

        print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
        print(f"{Colors.YELLOW}Nome:{Colors.RESET} {animal.nome}")
        print(f"{Colors.RED}❤️ Saúde:{Colors.RESET} {animal.status_bar(animal.health)} {animal.health}")
        print(f"{Colors.GREEN}🍖 Fome:{Colors.RESET} {animal.status_bar(animal.hunger)} {animal.hunger}")
        print(f"{Colors.BLUE}⚡ Energia:{Colors.RESET} {animal.status_bar(animal.energy)} {animal.energy}")
        print(f"{Colors.MAGENTA}😊 Felicidade:{Colors.RESET} {animal.status_bar(animal.happiness)} {animal.happiness}")
        print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")

    def get_choice(self):
        return input(f"{Colors.YELLOW}Escolha uma opção: {Colors.RESET}").strip()
