# Tic-Tac-Toe Code with Comments

# Function to print the current state of the board
def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "  # Add separators between columns
        
        print(row_str)
        if i != len(board) - 1:
            print("----------")  # Print a separator between rows

# Function to get a valid move from the player
def get_move(turn, board):
    while True:
        # Get the row and column from the player
        row = int(input("Row: "))
        col = int(input("Column: "))

        # Validate the row and column inputs
        if row < 1 or row > len(board):
            print("Invalid row. Please try again.")
        elif col < 1 or col > len(board[row - 1]):
            print("Invalid column. Please try again.")
        elif board[row - 1][col - 1] != " ":
            print("Cell is taken, please try again")
        else:
            break
    # Update the board with the player's move
    board[row - 1][col - 1] = turn

# Function to check if there is a winner
def checkmate(board, turn):
    # Define all possible winning lines (rows, columns, diagonals)
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    # Check if any of the winning lines are complete
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break
        if win:
            return True
    return False

# Initialize the game board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# Set the initial turn to "X"
turn = "X"
turn_number = 1

# Print the initial empty board
print_board(board)

# Main game loop
while turn_number < 9:
    print()
    print("It is the", turn, "player's turn. Please select your move")
    # Get the player's move
    get_move(turn, board)
    # Print the updated board
    print_board(board)
    # Check if the current player has won
    winner = checkmate(board, turn)
    if winner:
        break

    # Switch turns between "X" and "O"
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1

# Print the result of the game
if turn_number == 9:
    print()
    print_board(board)
    print("Game ends up in a draw! Amazing!")
else:
    print("The winner was", turn)

# Comments for Future Improvement:
# - Add input validation to ensure the user inputs numbers within the valid range.
# - Improve user experience by providing more descriptive prompts and messages.
# - Add functionality for replaying the game without restarting the script.
# - Implement a graphical interface to make the game more interactive and visually appealing.
# - Allow players to choose their symbols (e.g., "X" or "O").
