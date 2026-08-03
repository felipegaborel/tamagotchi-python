"""
Arquivo principal do projeto Tamagotchi.
"""

from colorama import Fore, Style, init

from src.animals.cat import Cat
from src.animals.dog import Dog
from src.animals.dragon import Dragon
from src.animals.rabbit import Rabbit
from src.ui.menu import limpar_tela, mostrar_menu

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

    animais = {
        "1": Dog,
        "2": Cat,
        "3": Rabbit,
        "4": Dragon,
    }

    pet = animais.get(opcao, Dog)(nome)

    while True:
        limpar_tela()

        pet.mostrar_status()

        opcao = mostrar_menu()

        if opcao == "1":
            pet.alimentar()

        elif opcao == "2":
            pet.brincar()

        elif opcao == "3":
            pet.dormir()

        elif opcao == "4":
            pet.banho()

        elif opcao == "5":
            pet.mostrar_status()
            input("\nPressione ENTER para continuar...")

        elif opcao == "6":
            print("\nAté logo!")
            break

        else:
            print("\nOpção inválida!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
