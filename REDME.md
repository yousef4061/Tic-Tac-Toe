# Tic Tac Toe

#### This project is a simple ***Tic Tac Toe*** game implemented in **python.** 
Two players can play against each other, and the game will determine the winner.

## Features

- Two-player mode on thr console
- Displays the winner or a draw
- Simple and easy-to-understand Python implementation

## How to Run

Fist, clone the repository or download the ***main.py***

## How to Play

- One player is "X" and the other is "O".
- Players take turns entering a number (1-9) to select a call.
- The game continues until one player wins or the match ends in a draw.

![alt text](pexels-jorgeromeroortiz-27115293.jpg)

## Project Structure


## Example Code

Here is a simple implementation of Tic Tac Toe in python:

```python
# Simple Tic Tac Toe Game in Python
board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
    print("_" * 5)

def play_game():
    for turn in range(9):
        move = int(input("Enter position (1-9): ")) -1

        board[move] = "x" if turn % 2 == 0 else "o"
        pront_board()
        # Check winner logic can be added here

play_game()
```    


## Contribution

If oyu want to contribute to this project, feel free to submit a pull request.

## license 

This project is released under the **MIT** license.