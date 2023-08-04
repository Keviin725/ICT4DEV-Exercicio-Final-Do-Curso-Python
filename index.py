def draw_board():
    
    print("A", end=" ")
    for i in range(3):
        if board[0][i] == 0:
            print("__", end=" ")
        elif board[0][i] == 1:
            print("X ", end=" ")
        else:
            print("O ", end=" ")
    print()
    print("B", end=" ")
    for i in range(3):
        if board[1][i] == 0:
            print("__", end=" ")
        elif board[1][i] == 1:
            print("X ", end=" ")
        else:
            print("O ", end=" ")
    print()
    print("C", end=" ")
    for i in range(3):
        if board[2][i] == 0:
            print("__", end=" ")
        elif board[2][i] == 1:
            print("X ", end=" ")
        else:
            print("O ", end=" ")
    print()

def ask_player(symbol):
 valid = False
 while not valid:
    move = input(f"Jogador {symbol}, escolha uma linha (A, B ou C) e uma coluna (1, 2 ou 3): ").upper()
    if len(move) == 2 and move[0] in "ABC" and move[1] in "123":
        row = ord(move[0]) - ord("A")
        col = int(move[1]) - 1
        if board[row][col] == 0:
            board[row][col] = symbol
            valid = True
        else:
            print("Essa posição já está ocupada. Tente outra.")
    else:
        print("Jogada inválida. Digite uma letra e um número.")

def check_winner():
 # Verifica as linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
# Verifica as colunas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
 # Verifica as diagonais
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
 # Verifica se há espaços vazios
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return None
 # Se não houver vencedor nem espaços vazios, é empate
    return 0

def play():
    mode = input("Escolha o modo de jogo: (1) Um jogador (2) Dois jogadores: ")
    if mode == "1":
        symbol = int(input("Escolha o seu símbolo: (1) X (2) O: "))
    if symbol == 1:
        computer = 2
    else:
        computer = 1
    turn = 1
    while True:
        draw_board()
        if turn % 2 == 0:
            if mode == "1" and turn == computer:
                print("Vez do computador.")
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                while board[row][col] != 0:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    board[row][col] = computer
            else:
                ask_player(2)
        else:
            if mode == "1" and turn == symbol:
                ask_player(symbol)
            else:
                ask_player(1)
        result = check_winner()
        if result != None:
            draw_board()
        if result == 0:
            print("Empate!")
        else:
            print(f"O jogador {result} ganhou!")
            break
        turn += 1

def get_players():
    player1 = input("Nome do jogador 1: ")
    player2 = input("Nome do jogador 2: ")
    if "\n" in player1 or ":" in player1 or "\n" in player2 or ":" in player2:
        print("Nomes inválidos. Não podem conter '\n' ou ':'.")
        return get_players()
    else:
        try:
            file = open("resultados.txt", "r")
            data = file.read()
            file.close()
            if player1 not in data:
                file = open("resultados.txt", "a")
                file.write(f"{player1}:0\n")
                file.close()
            if player2 not in data:
                file = open("resultados.txt", "a")
                file.write(f"{player2}:0\n")
                file.close()
        except FileNotFoundError:
            file = open("resultados.txt", "w")
            file.write(f"{player1}:0\n")
            file.write(f"{player2}:0\n")
            file.close()
            return player1, player2

def update_scores(player1, player2, result):
    file = open("resultados.txt", "r")
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        name, score = lines[i].split(":")
        if name == player1:
            if result == 1:
                score = int(score) + 2
            elif result == 0:
                score = int(score) + 1
                lines[i] = f"{name}:{score}\n"
            elif name == player2:
                if result == 2:
                    score = int(score) + 2
            elif result == 0:
                score = int(score) + 1
                lines[i] = f"{name}:{score}\n"
                file = open("resultados.txt", "w")
                file.writelines(lines)
                file.close()


get_players()
play()
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
result = check_winner()
update_scores(player1, player2, result)