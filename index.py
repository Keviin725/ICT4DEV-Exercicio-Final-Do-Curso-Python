# Importar o módulo os para manipular arquivos
import os

# Definir o tabuleiro como uma lista de 9 espaços vazios
tabuleiro = [" " for i in range(9)]

# Definir as possíveis combinações de vitória como uma lista de tuplas
vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # linhas horizontais
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # linhas verticais
            (0, 4, 8), (2, 4, 6)] # diagonais

# Definir uma função para mostrar o tabuleiro na tela
def mostrar_tabuleiro():
    print(tabuleiro[0] + "|" + tabuleiro[1] + "|" + tabuleiro[2])
    print("-+-+-")
    print(tabuleiro[3] + "|" + tabuleiro[4] + "|" + tabuleiro[5])
    print("-+-+-")
    print(tabuleiro[6] + "|" + tabuleiro[7] + "|" + tabuleiro[8])

# Definir uma função para verificar se um jogador ganhou o jogo
def verificar_vitoria(simbolo):
    for a, b, c in vitorias:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo:
            return True
    return False

# Definir uma função para verificar se o tabuleiro está cheio
def verificar_empate():
    return " " not in tabuleiro

# Definir uma função para obter a jogada do jogador humano
def jogada_humano():
    while True:
        posicao = input("Escolha uma posição de 1 a 9: ")
        if posicao.isdigit() and 1 <= int(posicao) <= 9:
            posicao = int(posicao) - 1
            if tabuleiro[posicao] == " ":
                tabuleiro[posicao] = "X"
                break
            else:
                print("Essa posição já está ocupada. Tente outra.")
        else:
            print("Entrada inválida. Digite um número de 1 a 9.")

# Definir uma função para obter a jogada do jogador computador usando o algoritmo minimax
def jogada_computador():
    # Definir uma função auxiliar para avaliar a pontuação de um estado do jogo
    def avaliar(simbolo):
        if verificar_vitoria(simbolo):
            return 1 # vitória do bot
        elif verificar_vitoria("X"):
            return -1 # derrota do bot
        else:
            return 0 # empate ou jogo incompleto

    # Definir uma função auxiliar para aplicar o algoritmo minimax recursivamente
    def minimax(profundidade, e_max):
        # Verificar se o jogo terminou ou se a profundidade máxima foi atingida
        if verificar_vitoria("O") or verificar_vitoria("X") or verificar_empate() or profundidade == 0:
            return avaliar("O"), None # retornar a pontuação e nenhuma posição

        # Inicializar a melhor pontuação e a melhor posição
        if e_max: # se é o turno do bot (maximizador)
            melhor_pontuacao = -float("inf") # infinito negativo
            melhor_posicao = None
        else: # se é o turno do humano (minimizador)
            melhor_pontuacao = float("inf") # infinito positivo
            melhor_posicao = None

        # Percorrer todas as posições livres do tabuleiro
        for i in range(9):
            if tabuleiro[i] == " ":
                # Simular a jogada na posição livre
                if e_max: # se é o turno do bot
                    tabuleiro[i] = "O"
                else: # se é o turno do humano
                    tabuleiro[i] = "X"

                # Chamar o algoritmo minimax para o próximo nível da árvore de decisão
                pontuacao, _ = minimax(profundidade - 1, not e_max)

                # Desfazer a jogada simulada
                tabuleiro[i] = " "

                # Atualizar a melhor pontuação e a melhor posição
                if e_max: # se é o turno do bot
                    if pontuacao > melhor_pontuacao: # se a pontuação é maior que a melhor pontuação
                        melhor_pontuacao = pontuacao # atualizar a melhor pontuação
                        melhor_posicao = i # atualizar a melhor posição
                else: # se é o turno do humano
                    if pontuacao < melhor_pontuacao: # se a pontuação é menor que a melhor pontuação
                        melhor_pontuacao = pontuacao # atualizar a melhor pontuação
                        melhor_posicao = i # atualizar a melhor posição

        # Retornar a melhor pontuação e a melhor posição
        return melhor_pontuacao, melhor_posicao

    # Chamar o algoritmo minimax para o estado atual do jogo com uma profundidade máxima de 9
    _, posicao = minimax(9, True)

    # Fazer a jogada na melhor posição encontrada
    tabuleiro[posicao] = "O"

# Definir uma função para salvar os resultados dos jogadores em um arquivo
def salvar_resultados(jogador1, jogador2, pontos1, pontos2):
    # Decidir o nome do arquivo em que salvar os resultados
    nome_arquivo = "resultados.txt"

    # Verificar se o arquivo já existe e ler os seus conteúdos
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
    else:
        conteudo = ""

    # Criar um dicionário para armazenar os resultados dos jogadores
    resultados = {}

    # Percorrer as linhas do conteúdo do arquivo e atualizar o dicionário
    for linha in conteudo.split("\n"):
        if linha:
            nome, pontos = linha.split(":")
            resultados[nome] = int(pontos)

    # Atualizar os resultados dos jogadores atuais no dicionário
    resultados[jogador1] = resultados.get(jogador1, 0) + pontos1
    resultados[jogador2] = resultados.get(jogador2, 0) + pontos2

    # Escrever os resultados atualizados no arquivo
    with open(nome_arquivo, "w") as arquivo:
        for nome, pontos in resultados.items():
            arquivo.write(nome + ":" + str(pontos) + "\n")

# Definir uma função para executar o jogo principal
def jogo_da_velha():
    # Mostrar as instruções do jogo
    print("Bem-vindo ao jogo da velha!")
    print("Você é o jogador X e o computador é o jogador O.")
    print("Escolha uma posição de 1 a 9 conforme o esquema abaixo:")
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")
    print()

    # Perguntar os nomes dos dois jogadores
    jogador1 = input("Digite o nome do jogador humano: ")
    jogador2 = "PC"

    # Iniciar o jogo com o jogador humano
    turno = "X"

    # Repetir até que alguém ganhe ou haja um empate
    while True:
        # Mostrar o tabuleiro atual
        mostrar_tabuleiro()
        print()

        # Verificar se o jogo terminou
        if verificar_vitoria("X"):
            print("Parabéns! Você ganhou o jogo!")
            # Atribuir 2 pontos ao vencedor e 0 ao perdedor
            salvar_resultados(jogador1, jogador2, 2, 0)
            break
        elif verificar_vitoria("O"):
            print("Que pena! Você perdeu o jogo!")
            # Atribuir 0 pontos ao perdedor e 2 ao vencedor
            salvar_resultados(jogador1, jogador2, 0, 2)
            break
        elif verificar_empate():
            print("O jogo terminou em empate!")
            # Atribuir 1 ponto a ambos os jogadores
            salvar_resultados(jogador1, jogador2, 1, 1)
            break

        # Alternar entre os jogadores
        if turno == "X":
            jogada_humano()
            turno = "O"
        else:
            jogada_computador()
            turno = "X"

# Chamar a função principal para iniciar o jogo
jogo_da_velha()