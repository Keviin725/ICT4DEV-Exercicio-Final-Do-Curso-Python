def draw_board():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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

draw_board()