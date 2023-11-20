import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board, player):
    while True:
        try:
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board, player):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = player

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)

    print_board(board)

    while True:
        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board, current_player)

        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
