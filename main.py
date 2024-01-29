# library imports here

import keyboard  # for key capture without echoing it on screen
import time  # for sleeping the thread so that key captures aren't too fast,
from BoardFunctions import Gameboard 


def main(size, win):
    gboard = Gameboard(size, win)  # object gboard is the game board
    gboard.clrscr()
    gboard.printboard()
    if gboard.size == 1:  # edge case for board size of 1*1
        if gboard.win == 2:
            print("You Win")
            print("Your Score is: ", gboard.ssasassadssdsscore)
            exit(0)
        else:
            print("You Lose")
            print("Your Score is: ", gboard.score)
            exit(0)
    while True:
        curmove = keyboard.read_key()  # it reads the key but doesn't display it on screen
        ans = gboard.gmove(curmove)
        gboard.clrscr()
        gboard.printboard()
        if ans == 2:
            print("You Lose")
            print("Your Score is: ", gboard.score)
            exit(0)
        elif ans == 3:
            print("You Win")
            print("Your Score is: ", gboard.score)
            exit(0)
        elif ans == 0:
            print("Invalid Move")
        time.sleep(0.25)  # sleeps the thread so that too many keypresses aren't captured easily


main(4, 2048)