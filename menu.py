from gameplay import game_mode, start_game
from utils import clear_screen

def menu(): 
    print("MENU PRINCIPAL\n")
    print("1- Jogar")
    print("2- Sair")

def interface(): 
    clear_screen()
    while True:
        menu();
        option = int(input("\nEscolha sua opção: "))

        match option:
            case 1:
                # print("Função jogar!")
                clear_screen()
                #Escolher Dificuldade
                gameMode = game_mode()
                start_game(gameMode)
            case 2:
                clear_screen()
                print("Saindo...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

        