#LOOP WILL GO FOREVER IF NEITHER OF THE PLAYERS CAN REACH 20 YES I SET WINNING POINT 20 INSTEAD OF 100 CAUSE YOU KNOW IT WAS TAKING A LOT OF TIME FOR A PLAYER TO REACH 100 
#ANY MODIFICATION CAN BE DONE.

import random
import time

player1 = str(input("ENTER PLAYER 1 NAME: "))
player2 = str(input("ENTER PLAYER 2 NAME: "))
print(f"{player1}'s opponent is {player2}")
player1Pos = 0
player2Pos = 0
snakeorno = ["snake", "move"]


def Player1roll():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    moveorno = snakeorno[random.randint(0, 1)]
    if moveorno == "move":
        add = num1 + num2
        player1Pos = add
        result = (num1, num2)
        print(f"{player1} rolled {result}, move by {add} your position is {player1Pos}")

    elif moveorno == "snake":
        player1Pos = num1 - random.randint(1, 5)
        if player1Pos < 0:
            player1Pos = 0
            print(f"{player1} landed on snake so bye bye ur position is {player1Pos} since your position was coming negative it was set to 0")

        else:
            print(f"{player1} landed on snake so bye bye ur position is {player1Pos}")


def Player2roll():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    moveorno = snakeorno[random.randint(0, 1)]
    if moveorno == "move":
        add = num1 + num2
        player2Pos = add
        result = (num1, num2)
        print(f"{player2} rolled {result}, move by {add} your position is {player2Pos}")

    elif moveorno == "snake":
        player2Pos = num1 - random.randint(1, 5)
        if player2Pos < 0:
            player2Pos = 0
            print(
                f"{player2} landed on snake so bye bye ur position is {player2Pos} since your position was coming negative it was set to 0")

        else:
            print(f"{player2} landed on snake so bye bye ur position is {player2Pos}")


while player1Pos or player2Pos != 20:
    Player1roll()
    if player1Pos != 20:
        time.sleep(1)
        Player2roll()

if player1Pos == 20:
    print(f"{player1} won sorry but {player2} lost")
elif player2Pos == 20:
    print(f"{player2} won sorry but {player1} lost")
