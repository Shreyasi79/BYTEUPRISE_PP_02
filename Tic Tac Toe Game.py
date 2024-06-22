def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_full(board):
    return all([cell != " " for row in board for cell in row])


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    while not winner and not is_full(board):
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                winner = current_player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")
tic_tac_toe()
