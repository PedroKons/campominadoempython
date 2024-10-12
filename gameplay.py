from utils import clear_screen, color_cell
import numpy as np
from load import return_rows_cols_data, insert_boom_data

def game_mode():
    clear_screen()
    while True:
        print("\n1- Fácil(Aqui você joga com um campo de 5x5)")
        print("\n2- Médio(Aqui você joga com um campo de 8x8)")
        print("\n3- Difícil(Aqui você joga com um campo de 12x12)")
    
        option = int(input("\nQual dificuldade você quer jogar?: "))
        
        match option:
            case 1:
                clear_screen()
                return "easy"
            case 2:
                clear_screen()
                return "medium"
            case 3:
                clear_screen()
                return "hard"
            case _:
                print("\nOpção inválida! Tente novamente.\n")

def check_boom(table, cols, rows):
    if table[rows][cols] == 1:
        return True
    else:
        return False
    
def count_bombs_around(table, row, col, rows, cols):  # Define a função que conta bombas ao redor de uma célula na tabela
    bombsCount = 0  # Inicializa o contador de bombas como 0
    # Verifica as 8 direções ao redor da célula
    for i in range(-1, 2):  # Percorre as linhas adjacentes: uma linha acima (-1), a linha atual (0), e uma linha abaixo (+1)
        for j in range(-1, 2):  # Percorre as colunas adjacentes: uma coluna à esquerda (-1), a coluna atual (0), e uma coluna à direita (+1)
            if i == 0 and j == 0:  # Se está na célula central (a própria célula que está sendo verificada)
                continue  # Pula essa célula, pois não queremos contar ela mesma
            newRow, newCol = row + i, col + j  # Calcula as coordenadas da célula adjacente (nova linha e nova coluna)
            # Verifica se a célula adjacente está dentro dos limites da tabela
            if 0 <= newRow < rows and 0 <= newCol < cols:  # Checa se a nova linha e coluna estão dentro dos limites da tabela
                if table[newRow][newCol] == 1:  # Se a célula adjacente contém uma bomba (1 representa uma bomba)
                    bombsCount += 1  # Incrementa o contador de bombas
    return bombsCount  # Retorna o número total de bombas encontradas ao redor da célula


def reveal_bombs(table, displayTable, rows, cols):
    # Revela todas as bombas na tabela de exibição
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                displayTable[i][j] = 'B'  # Mostra a bomba com um símbolo 'B'  

def check_win(table, displayTable, rows, cols):
    for i in range(rows):
        for j in range(cols):
            # Se a célula não for uma bomba (valor 1) e ainda estiver com "#", o jogo ainda não foi vencido
            if table[i][j] == 0 and displayTable[i][j] == "#":
                return False
    return True

def verification_input(inputVerif, limit):
    try:
        # Converte a entrada para inteiro
        inputVerif = int(inputVerif)

        # Verifica se está no intervalo
        if 0 <= inputVerif <= limit:
            return inputVerif
        else:
            print(f"Entrada fora do intervalo. Digite um número entre 0 e {limit}.")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return None

def reveal_adjacent_cells(table, displayTable, row, col, rows, cols):
    # Se já foi revelada, retorna
    if displayTable[row][col] != "#":
        return
    
    bombs_around = count_bombs_around(table, row, col, rows, cols)
    
    if bombs_around == 0:
        displayTable[row][col] = "-"  # Revela como vazio
        # Se não há bombas ao redor, revela as células adjacentes recursivamente
        for i in range(-1, 2):
            for j in range(-1, 2):
                newRow, newCol = row + i, col + j
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    reveal_adjacent_cells(table, displayTable, newRow, newCol, rows, cols)
    else:
        displayTable[row][col] = str(bombs_around)  # Se há bombas ao redor, mostra o número de bombas

def start_game(gameMode):

    if gameMode == "easy":
        rows, cols = return_rows_cols_data(gameMode)
    elif gameMode == "medium":
        rows, cols = return_rows_cols_data(gameMode)
    elif gameMode == "hard":
        rows, cols = return_rows_cols_data(gameMode)
    else:
        print("\nModo de jogo inválido!\n")
        return

    table = np.zeros((rows, cols), dtype=int) # diz que cada linha é um int
    displayTable = np.full((rows, cols), "#")  # Inicialmente, todas as casas são "#"
    win = False
    boom = False

    insert_boom_data(table, rows, cols, gameMode)

    while True:
        print("   " + " ".join([str(i) for i in range(cols)]))

        for i, row in enumerate(table): #vizualizar o gabarito de bomba
            print(f"{i}  " + " ".join(map(str, row)))

        print("\n")

        print("   " + " ".join([str(i) for i in range(cols)]))

        # Exibe a tabela de jogo
        for i, row in enumerate(displayTable):
            colored_row = " ".join([color_cell(cell) for cell in row])  # Colore cada célula
            print(f"{i}  " + colored_row)
        
        while True:
            print("\nFaça sua jogada de acordo com as coordenadas\n")
            # Solicita entrada e verifica
            inputUserRows = verification_input(input("Digite a linha: "), rows)
            inputUserCols = verification_input(input("Digite a Coluna: "), rows)

            # Verifica se as duas entradas são válidas
            if inputUserRows is not None and inputUserCols is not None:
                break  # Sai do loop se as entradas forem válidas

        if check_boom(table, inputUserCols, inputUserRows):
            clear_screen()
            print("\n Você acertou uma bomba!\n")
            boom = True
            reveal_bombs(table, displayTable, rows, cols) 
        else:
            clear_screen()
            print("\n Não acertou nenhuma bomba")
            reveal_adjacent_cells(table, displayTable, inputUserRows, inputUserCols, rows, cols)

        if check_win(table, displayTable, rows, cols):
            clear_screen()
            print("Você Ganhou, Parabéns!")
            win = True
            print("\nAperte Enter Para Reiniciar")
            input()
            break

        if boom == True :
            print("   " + " ".join([str(i) for i in range(cols)]))

            # Revela a tabela com as bombas ao final do jogo
            for i, row in enumerate(displayTable):  # Exibe a tabela revelada
                colored_row = " ".join([color_cell(cell) for cell in row])
                print(f"{i}  " + colored_row)
            print("\nVocê Perdeu, Mais sorte na próxima!\n")
            print("\nAperte Enter Para Reiniciar")
            input()
            break

