# Ask the user to input a chess piece between two pieces of your choice and where it is on the board.
# The choice should be made by writing the piece and the coordinates in a predefined format in the console, e.g.: knight a5.

# The user is asked to enter the black pieces, one by one, in the same format as the white piece.
# They need to add at least 1 black piece or 16 at most. Once at least one black piece has been added, the user can write “done” instead of the coordinates to add no more pieces.

# After adding each piece, there should be either a confirmation that it was added successfully, or an error message explaining what the issue is.

# After the white and the black pieces are added, the program should print out the black pieces, if any, that the white piece can take.
# -------------

def main():
    # iniciate white_move function and store results in white_result
    white_result = white_move()
    if white_result is None or white_result[0] is None: # 1st element in white_result, a.k.a white_piece
        print("Game over.")
        return # stop program if white move has no correct values

    white_piece, white_coord = white_result # needed for checking of already taken spots: for black_move(white_cord)

    # iniciate black_move function and store results in black_postitions
    black_positions = black_move(white_coord)
    if not black_positions:
        print("No valid black pieces entered to continue. Game over.")
        return  # stop program if black move has no correct values

    # calculate and show captures for rook
    if white_result[0] == "rook":
        captures = calculate_rook_captures(white_result[1], black_positions) # 2nd element in white_result, a.k.a white_coord
        if captures: # or in other word capture is True
            print(f"The rook at {white_result[1]} can capture black pieces at: {captures}")
        else:
            print(f"The rook at {white_result[1]} cannot capture any black pieces.")
    # calculate and show captures for pawn
    elif white_result[0] == "pawn":
        captures = calculate_pawn_captures(white_result[1], black_positions)
        if captures:
            print(f"The pawn at {white_result[1]} can capture black pieces at: {captures}")
        else:
            print(f"The pawn at {white_result[1]} cannot capture any black pieces.")

# User input for white piece, its coordinates and validation.
def white_move():
    try: # check for correct input format (try-except)
        white_input = input("Which WHITE figure you will choose: pawn or rook? And where to place it on the board, e.g.: pawn a5? -> ").lower() # ask for user input of white figure
        white_piece, white_coord = white_input.split(" ") # split answer in order to check validity
        column, row = white_coord[0], white_coord[1] # split to check correct coordinates values

        # check for right figure
        if white_piece not in ["pawn", "rook"]:
            print("Wrong piece! Choose 'pawn' or 'rook'.")
            return None

        # check if the column is in board: 1-8, a-h
        if column not in "abcdefgh" or row not in "12345678":
            print("Invalid coordinate. Column must be from 'a' to 'h' and row must be from '1' to '8'.")
            return None

        print("Successful white move.")
        return white_piece, white_coord # return value for captures step

    except ValueError:
            print("Wrong white input. Please use 'piece coord' format. ")
            return None

# User input for black pieces, its coordinates and validation.
def black_move(white_coord): # parameter to check for white pieces spot
    black_positions = [] # keep black piecces positions
    i = 0
    while True:
        black_input = input("Place a BLACK figure (e.g.: pawn a5) or just write 'done' -> ").lower() # ask for user input of black figure
        if black_input=="done":
            break
        if i >= 16:  # Allow up to 16 black pieces
            print("Maximum of 16 black pieces reached.")
            break

        try: # check for correct input format (try-except)
            black_piece, black_coord = black_input.split(" ") # split answer in order to check validity
            bl_col, bl_row = black_coord[0], black_coord[1] # split to check correct coordinates values

            # check for right figure
            if black_piece not in ["pawn", "rook", "knight", "bishop", "queen", "king"]:
                print("Wrong piece. ")
                return None

            # check if the column is in board: 1-8, a-h
            if bl_col not in "abcdefgh" or bl_row not in "12345678":
                print("Invalid coordinate. Column must be from 'a' to 'h' and row must be from '1' to '8'.")
                return None

            # check if there is already a white piece
            if black_coord == white_coord:
                print("Place is already taken by white piece.")
                return None

            print("Successful black move.")
            black_positions.append(black_coord) # adds to the black_positions list:

        except ValueError:
            print("Wrong input. Please use 'piece coord' format. Program will stop.")
            return None
        i +=1
    return black_positions

# check all possible moves and attacks for rook
def calculate_rook_captures(rook_position, black_positions):
    rook_column, rook_row = rook_position[0], rook_position[1]
    captures = [] # list for possible captures

    # Calculate horizontal moves
    for col in "abcdefgh":
        if col != rook_column: # skip current position
            move = col + rook_row # checks horizontally every move
            if move in black_positions: # checks if move is already added to black list
                captures.append(move) # adds to capture list
    # Calculate vertical moves
    for row in "12345678":
        if row != rook_row:
            move = rook_column + row
            if move in black_positions:
                captures.append(move)
    return captures

# check all possible moves and attacks for pawn
def calculate_pawn_captures(pawn_position, black_positions):
    pawn_col, pawn_row = ord(pawn_position[0]), int(pawn_position[1]) # ord() converts letter to number; int() number->integer
    captures = []

    # Check diagonal captures (one square forward and one square to either side)
    capture_squares = [
        chr(pawn_col - 1) + str(pawn_row + 1) if pawn_col > ord('a') else None,
        chr(pawn_col + 1) + str(pawn_row + 1) if pawn_col < ord('h') else None
    ]

    for square in capture_squares:
        if square and square in black_positions:
            captures.append(square)
    return captures


# call main function
if __name__ == "__main__":
    main()
