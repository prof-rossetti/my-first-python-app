import os
import random

from game_utils.rock_paper_scissors import determine_winner # see: https://github.com/s2t2/game-utils-py
from dotenv import load_dotenv # see: ________

load_dotenv()

USER_NAME = os.getenv("USER_NAME", default="Player One")

if __name__ == "__main__":

    print("-------------------")
    print("WELCOME TO MY ROCK-PAPER-SCISSORS GAME!!")

    print("-------------------")
    print("PLEASE SELECT ONE OF THE FOLLOWING OPTIONS:")
    options = ["rock", "paper", "scissors"]
    print(options)

    print("-------------------")
    user_choice = "rock" # TODO: accept user input
    print("YOU CHOSE:", user_choice)

    print("-------------------")
    computer_choice = random.choice(options)
    print("COMPUTER CHOSE:", computer_choice)

    print("-------------------")
    winning_choice = determine_winner(user_choice, computer_choice)
    print("WINNING CHOICE:", winning_choice)

    print("-------------------")
    print("THANKS, PLEASE PLAY AGAIN!")
    print("-------------------")

    #breakpoint()
    #print(dir(random))
    #print(help(random.choice)) # then press "q" to quit
    #print(type(options))
    #print(type(user_choice))
