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

    nome = input("\nDigite o nome do seu pet: ")

    print("\nEscolha um animal:")
    print("1 - Cachorro")
    print("2 - Gato")
    print("3 - Coelho")
    print("4 - Dragão")

    opcao = input("\nSua escolha: ")


if __name__ == "__main__":
    main()
