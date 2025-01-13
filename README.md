# A Chess Project

This Python program simulates a chess piece capture game. Users can input the position of a white piece (either a pawn or a rook) and place black pieces on the board. The program then calculates and displays which black pieces, if any, the white piece could capture in any possible way. If user inputs at least one "wrong" piece, a program will stop.

## Features

- Allows users to place a white piece (pawn or rook) on the board by specifying its type and position.
- Accepts input for up to 16 black pieces and validates their positions.
- Ensures no overlap between black pieces and the white piece.
- Calculates valid capture moves for the white piece:
  - For a **rook**, captures are based on horizontal and vertical moves.
  - For a **pawn**, captures are based on diagonal moves.

## How to Use

1. **Run the Program**  
   Start the program in your Python environment.

2. **Input the White Piece**  
   Enter the type and position of the white piece in the format `piece position`, e.g., `rook a5` or `pawn b3`.

3. **Input the Black Pieces**  
   Enter each black piece in the format `piece position`, e.g., `pawn d4`.  
   - Enter `done` to finish placing black pieces.
   - The maximum number of black pieces allowed is 16.

4. **View the Result**  
   The program will display:
   - The black pieces that the white piece can capture.
   - A message if no captures are possible.

![image](https://github.com/user-attachments/assets/ab3d54b6-d3c5-446a-99c0-32f06d95681a)
