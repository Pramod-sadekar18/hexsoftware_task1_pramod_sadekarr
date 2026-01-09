import random

def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],   
        [0,4,8], [2,4,6]             
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False



def check_draw(board):
    return " " not in board


def player_move(board):
    while True:
        move = input("Choose a position (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
        print("❌ Invalid move. Try again.")



def computer_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"
    print(f"🤖 Computer chose position {move + 1}")



def play_game():
    board = [" "] * 9
    print("🎮 Welcome to Tic-Tac-Toe")
    print("You are X | Computer is O")
    print("Positions are 1 to 9")

    display_board(board)

    while True:
        player_move(board)
        display_board(board)

        if check_win(board, "X"):
            print("🎉 Congratulations! You win!")
            break

        if check_draw(board):
            print("😐 It's a Draw!")
            break

   
        computer_move(board)
        display_board(board)

        if check_win(board, "O"):
            print("🤖 Computer wins!")
            break

        if check_draw(board):
            print("😐 It's a Draw!")
            break


play_game()
