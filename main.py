"""
Arquivo principal do projeto Tamagotchi.
"""

from colorama import Fore, Style, init

init(autoreset=True)


def main() -> None:
    print(Fore.GREEN + "=" * 50)
    print(Fore.CYAN + "🐶 TAMAGOTCHI PYTHON")
    print(Fore.GREEN + "=" * 50)
    print("\nProjeto inicializado com sucesso!")
    print(Style.BRIGHT + "Bem-vindo ao Tamagotchi Python!\n")


if __name__ == "__main__":
    main()
