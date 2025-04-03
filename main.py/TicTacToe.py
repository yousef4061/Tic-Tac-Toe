import pyfiglet
import random

def show():
    for row in game_board:
        print(" ".join(row)) 


def check_game():
    lines = game_board + [list(x) for x in zip(*game_board)] + [[game_board[i][i] for i in
    range(3)]] + [[game_board[i][2-i] for i in range(3)]]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != "_":
            print(f"player {'1' if line[0] == 'x' else '2'} wins!")
            winner = "player 1 🎉" if line[0] == "x" else "player 2 🎉"
            print(f"🎊🎊 {winner} barande shod! 🎊🎊")
            return True
    return False
        
title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

mode = ""
while mode not in ["2p", "cpu"]:
    mode = input("do you want to play with a friend or (2p) or against the computer (cpu)? (2p/cpu):").strip().lower()

game_board = [["_"] * 3 for _ in range(3)]
show()

while True:
    for player, symbol in [("1", "x"), ("2", "o")]:
        print(f"player {player}")
        if mode == "cpu" and player == "2":
            while True:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if game_board[row][col] == "_":
                    game_board[row][col] = symbol
                    break
            print(f"computer played at: {row}{col}")
                    
        else:
            while True:
                try:
                    row = int(input("enter row (0-2):"))
                    col = int(input("enter col (0-2):"))

                    if 0 <= row <= 2 and 0 <= col <= 2 and game_board[row][col] == "_":
                        game_board[row][col] = symbol
                        break
                    print("jer nazan :/")
                except ValueError: 
                    print("mese adam vared kon :|")

        show()
        if check_game():
            exit()