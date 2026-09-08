"""
Arquivo principal do projeto Tamagotchi.
"""

from colorama import Fore, Style, init

from src.animals.cat import Cat
from src.animals.dog import Dog
from src.animals.dragon import Dragon
from src.animals.rabbit import Rabbit
from src.game.game import Game
from src.ui.banner import BANNER
from src.ui.menu import limpar_tela, mostrar_menu

init(autoreset=True)


def main() -> None:
    print(BANNER)
    print(Fore.GREEN + "=" * 50)
    print(Fore.CYAN + "🐶 TAMAGOTCHI PYTHON")
    print(Fore.GREEN + "=" * 50)
    print("\nProjeto inicializado com sucesso!")
    print(Style.BRIGHT + "Bem-vindo ao Tamagotchi Python!\n")

    nome = input("\nDigite o nome do seu pet: ").strip() or "Tama"

    animais = {
        "1": Dog,
        "2": Cat,
        "3": Rabbit,
        "4": Dragon,
    }

    # Validação da escolha do animal — repete até o usuário fornecer uma opção válida
    while True:
        print("\nEscolha um animal:")
        print("1 - Cachorro")
        print("2 - Gato")
        print("3 - Coelho")
        print("4 - Dragão")

        escolha = input("\nSua escolha (padrão 1): ").strip()
        if escolha == "":
            escolha = "1"

        if escolha in animais:
            break

        print(Fore.YELLOW + "Opção inválida. Tente novamente.")

    pet = animais[escolha](nome)
    game = Game()

    try:
        while True:
            limpar_tela()

            game.verificar_vida(pet)
            if not pet.vivo:
                break

            pet.mostrar_status()

            menu_opcao = mostrar_menu()

            if menu_opcao == "1":
                pet.alimentar()
            elif menu_opcao == "2":
                pet.brincar()
            elif menu_opcao == "3":
                pet.dormir()
            elif menu_opcao == "4":
                pet.banho()
            elif menu_opcao == "5":
                # Mostra status e pausa — evitar dupla pausa exibida mais abaixo
                pet.mostrar_status()
                input("\nPressione ENTER para continuar...")
                continue
            elif menu_opcao == "6":
                print("\nAté logo!")
                break
            else:
                print("\nOpção inválida!")

            # Pausa padrão após ações que não exibem o status completo
            input("\nPressione ENTER para continuar...")
    except KeyboardInterrupt:
        print("\n\nEncerrando jogo... Até logo!")


if __name__ == "__main__":
    main()
