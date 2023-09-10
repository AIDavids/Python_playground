# Rock Paper Scissor
import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
user = input("rock, paper or scissors")
user = user.lower()
if user != "rock" and user != "paper" and user != "scissors":
    print("Wrong input")
if user == computer:
    print("Draw")
elif user == "scissors":
    if computer == "paper":
        print("You win")
    if computer == "rock":
        print("You lose")
elif user == "rock":
    if computer == "paper":
        print("You lose")
    if computer == "scissors":
        print("You win")
elif user == "paper":
    if computer == "rock":
        print("You lose")
    if computer == "scissors":
        print("You win")