def return_rows_cols_data(gameMode):
    if gameMode == "easy":
        with open('c:/Users/Pedro/Documents/VS CODE/campominadoempython/.data/easy.txt', 'r') as file:
            # Lendo a primeira linha do arquivo
            primeira_linha = file.readline().strip()
        # Convertendo a primeira linha para inteiro
        linhas, colunas = int(primeira_linha[0]), int(primeira_linha[1])

        return linhas,colunas
    elif gameMode == "medium":
        with open('c:/Users/Pedro/Documents/VS CODE/campominadoempython/.data/medium.txt', 'r') as file:
            # Lendo a primeira linha do arquivo
            primeira_linha = file.readline().strip()
        # Convertendo a primeira linha para inteiro
        linhas, colunas = int(primeira_linha[0]), int(primeira_linha[1])

        return linhas,colunas
    elif gameMode == "hard":
        with open('c:/Users/Pedro/Documents/VS CODE/campominadoempython/.data/hard.txt', 'r') as file:
            # Lendo a primeira linha do arquivo
            primeira_linha = file.readline().strip()
            # Pegando os primeiros dois números como "12" para linhas e "12" para colunas
            linhas = int(primeira_linha[:2])  # Pegando os dois primeiros caracteres "12"
            colunas = int(primeira_linha[2:4])  # Pegando os dois seguintes "12"
            
        return linhas,colunas

def insert_boom_data(table, rows, cols, gameMode):

    if gameMode == "easy":
        with open('c:/Users/Pedro/Documents/VS CODE/campominadoempython/.data/easy.txt', 'r') as file:
            file.readline()

            # Lendo a tabela restante e inserindo os valores na tabela passada como parâmetro
            for i in range(rows):
                linha = list(map(int, file.readline().strip().split()))  # Converte cada linha em uma lista de inteiros
                for j in range(cols):
                    table[i][j] = linha[j]  # Copia os valores para a tabela
    
    if gameMode == "medium":
        with open('c:/Users/Pedro/Documents/VS CODE/campominadoempython/.data/medium.txt', 'r') as file:
            file.readline()

            # Lendo a tabela restante e inserindo os valores na tabela passada como parâmetro
            for i in range(rows):
                linha = list(map(int, file.readline().strip().split()))  # Converte cada linha em uma lista de inteiros
                for j in range(cols):
                    table[i][j] = linha[j]  # Copia os valores para a tabela

    if gameMode == "hard":
        with open('c:/Users/Pedro/Documents/VS CODE/campominadoempython/.data/hard.txt', 'r') as file:
            file.readline()

            # Lendo a tabela restante e inserindo os valores na tabela passada como parâmetro
            for i in range(rows):
                linha = list(map(int, file.readline().strip().split()))  # Converte cada linha em uma lista de inteiros
                for j in range(cols):
                    table[i][j] = linha[j]  # Copia os valores para a tabela