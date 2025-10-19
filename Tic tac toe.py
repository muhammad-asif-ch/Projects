import math
import time
import sys

# --- Initialize Board ---
board = [" " for _ in range(9)]
AI = "O"
HUMAN = "X"

# --- Print Board Function ---
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")

# --- Check Winner Function ---
def check_winner(board):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != " ":
            return board[cond[0]]
    if " " not in board:
        return "Draw"
    return None

# --- AI Thinking Animation ---
def ai_thinking():
    text = "AI is thinking"
    for dot_count in range(4):
        sys.stdout.write("\r" + text + "." * dot_count + " " * (3 - dot_count))
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

# --- Minimax with Alpha-Beta Pruning ---
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == "Draw":
        return 0
# Alpha beta purning
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <=alpha :
                    break  # prune
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # prune
        return min_eval

# --- AI Move Function ---
def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# --- Main Game Loop ---
def play_game():
    print("Tic Tac Toe using Minimax + Alpha-Beta Pruning\n")
    print_board(board)

    while True:
        # --- Human Move ---
        move = input("Enter your move (1-9): - X ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Please enter a number between 1 and 9.")
            continue

        move = int(move) - 1
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = HUMAN
        print_board(board)

        if check_winner(board):
            winner = check_winner(board)
            if winner == "Draw":
                print("It's a Draw!")
            else:
                print(f"Winner is: {winner}")
            break

        # --- AI Move ---
        ai_thinking()
        ai_move = best_move(board)
        board[ai_move] = AI
        print_board(board)

        if check_winner(board):
            winner = check_winner(board)
            if winner == "Draw":
                print("It's a Draw!")
            else:
                print(f"Winner is: {winner}")
            break

# --- Run the Game ---
if __name__ == "__main__":
    play_game()
