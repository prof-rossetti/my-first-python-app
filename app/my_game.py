import os
import random

from game_utils.rock_paper_scissors import determine_winner # see: https://github.com/s2t2/game-utils-py
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME", default="Player One")

OPTIONS = ["rock", "paper", "scissors"]

if __name__ == "__main__":

    print("-------------------")
    print("WELCOME TO MY ROCK-PAPER-SCISSORS GAME!!")
    print(f"PLAYER: '{USER_NAME}'")

    print("-------------------")
    print("PLEASE SELECT ONE OF THE FOLLOWING OPTIONS:", OPTIONS)

    print("-------------------")
    user_choice = "rock" # TODO: accept user input
    print(f"YOU CHOSE: '{user_choice}'")

    computer_choice = random.choice(OPTIONS)
    print(f"COMPUTER CHOSE: '{computer_choice}'")

    winning_choice = determine_winner(user_choice, computer_choice)
    print(f"Great your guess is right \n Wow, you won ;-) \ n WINNING CHOICE: '{winning_choice}'")

    print("-------------------")
    print("THANKS, PLEASE PLAY AGAIN!")
    print("-------------------")

    #breakpoint()
    #print(dir(random))
    #print(help(random.choice)) # then press "q" to quit
    #print(type(options))
    #print(type(user_choice))
