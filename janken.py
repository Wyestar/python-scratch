# import asyncio

import random
import sys

print("Rock paper scissors!")
print(
    "Play either 'rock', 'paper', or 'scissors' by typing them then pressing enter. The computer will randomly play one of the three."
)
# print("rock beats scissors")
# print("scissors beats paper")
# print("paper beats rock")


def janken():
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    possiblePlays = [rock, paper, scissors]

    stop = "y"

    while stop == "y":
        userPlay = input("What will you play? > ")

        # check user play is valid
        if userPlay not in possiblePlays:
            print("You must play either 'rock', 'paper', or 'scissors'")
            continue

        # set cpu play with rng
        randomIndex = random.randint(0, 2)
        cpuPlay = possiblePlays[randomIndex]

        if userPlay == cpuPlay:
            print("It's a tie! Play again?")

        elif userPlay == rock:
            if cpuPlay == scissors:
                print("You win! Play again?")
            elif cpuPlay == paper:
                print("You lose! Play again?")

        elif userPlay == paper:
            if cpuPlay == rock:
                print("You win! Play again?")
            elif cpuPlay == scissors:
                print("You lose! Play again?")

        elif userPlay == scissors:
            if cpuPlay == paper:
                print("You win! Play again?")
            elif cpuPlay == rock:
                print("You lose! Play again?")

        print("The CPU played: ", cpuPlay)
        stop = input("Play again? (y/n) > ")

    print("Thank you for playing!")

    return


janken()

# ===
# from flask import Flask, render_template, request, session

# app = Flask(__name__)

# @app.route("/")
# def index():

# @app.route("/play", methods=["POST"])
# def rpsPlay():
# player_choice = request.form["choice"]
