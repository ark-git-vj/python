def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    # Check for tie
    if " " not in board:
        return "Tie"
    
    return None

def main():
    board = [" " for _ in range(9)]
    current_player = "X"
    winner = None
    
    print("\nWelcome to Tic Tac Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom")
    print("1 | 2 | 3")
    print("-----------")
    print("4 | 5 | 6")
    print("-----------")
    print("7 | 8 | 9\n")
    
    while not winner:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        while True:
            try:
                position = int(input("Enter position (1-9): ")) - 1
                if 0 <= position <= 8 and board[position] == " ":
                    break
                else:
                    print("Invalid position! Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9!")
        
        board[position] = current_player
        winner = check_winner(board)
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    if winner == "Tie":
        print("\nGame Over! It's a tie!")
    else:
        print(f"\nGame Over! Player {winner} wins!")

if __name__ == "__main__":
    while True:
        main()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
