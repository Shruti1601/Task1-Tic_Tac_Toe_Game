import random

# Define the Tic Tac Toe board
board = [" " for _ in range(9)]

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to check if the game is over
def is_game_over(board):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return is_board_full(board)

# Function to evaluate the board for the AI player
def evaluate(board):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == "X":
            return 1
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] == "O":
            return -1
    return 0

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if is_game_over(board):
        return evaluate(board)
    
    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the best move for the AI player
def best_move(board):
    best_eval = float("-inf")
    best_move = -1
    alpha = float("-inf")
    beta = float("inf")
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 0, False, alpha, beta)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    
    return best_move

# Main game loop
while True:
    print_board(board)
    
    if is_board_full(board):
        print("It's a draw!")
        break
    
    player_move = int(input("Enter your move (0-8): "))
    
    if board[player_move] == " ":
        board[player_move] = "O"
    else:
        print("Invalid move. Try again.")
        continue
    
    if is_game_over(board):
        print_board(board)
        print("You win!")
        break
    
    ai_move = best_move(board)
    board[ai_move] = "X"
    
    if is_game_over(board):
        print_board(board)
        print("AI wins!")
        break
