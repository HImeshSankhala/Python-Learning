# 2048 Game Implementation

This project implements the popular 2048 game using Python. The game logic is separated into a `logic.py` file, while the main game interface and execution are handled in the `2048.py` file.

## How to Play

The goal of the game is to combine tiles with the same number to create a tile with the number 2048. Use the following commands to move the tiles on the board:

- **'W' or 'w'**: Move Up
- **'S' or 's'**: Move Down
- **'A' or 'a'**: Move Left
- **'D' or 'd'**: Move Right

## Files

- `logic.py`: Contains all the game logic functions.
- `2048.py`: Main file to run the game and interact with the user.

## Running the Game

1. Ensure you have Python installed on your system.
2. Clone this repository or download the files `logic.py` and `2048.py`.
3. Open a terminal and navigate to the directory containing the files.
4. Run the game using the following command:
   ```bash
   python 2048.py
   ```
5. Follow the on-screen instructions to play the game.

## Game Logic

### `logic.py`

- `start_game()`: Initializes the game grid and adds two '2' tiles to random positions.
- `add_new_2(mat)`: Adds a '2' tile to a random empty position on the grid.
- `get_current_state(mat)`: Checks the current state of the game - 'WON', 'GAME NOT OVER', or 'LOST'.
- `compress(mat)`: Compresses the grid to the left.
- `merge(mat)`: Merges the tiles in the grid.
- `reverse(mat)`: Reverses the rows of the grid.
- `transpose(mat)`: Transposes the grid (interchanges rows and columns).
- `move_left(grid)`: Moves tiles to the left.
- `move_right(grid)`: Moves tiles to the right.
- `move_up(grid)`: Moves tiles up.
- `move_down(grid)`: Moves tiles down.

### `2048.py`

- `print_grid(mat)`: Prints the game grid.
- `main()`: Runs the main game loop, processing user inputs and updating the game state.

## Time and Space Complexity

### Time Complexity

- **Initialization (`start_game` and `add_new_2`)**: O(1) for adding a new '2' tile.
- **State Check (`get_current_state`)**: O(n^2), where n is the dimension of the grid (4x4 in this case).
- **Compression (`compress`)**: O(n^2) for iterating through each cell in the grid.
- **Merge (`merge`)**: O(n^2) for iterating through each cell in the grid.
- **Reverse (`reverse`)**: O(n^2) for iterating through each cell in the grid.
- **Transpose (`transpose`)**: O(n^2) for iterating through each cell in the grid.
- **Move Operations (`move_left`, `move_right`, `move_up`, `move_down`)**: O(n^2) for compressing, merging, and potentially compressing again.

Overall, each move operation has a time complexity of O(n^2), where n is the dimension of the grid.

### Space Complexity

- The space complexity is O(n^2) for storing the game grid.
- Additional space is used for temporary grids in functions like `compress`, `reverse`, and `transpose`, but this does not change the overall space complexity of O(n^2).

Given the fixed size of the grid (4x4), these complexities are manageable and ensure efficient performance for the game.
