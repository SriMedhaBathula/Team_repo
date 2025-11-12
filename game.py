import random

def rock_paper_scissor():
    return random.choice(["rock", "paper", "scissors"])

choice = rock_paper_scissor()

print("Welcome to Rock-Paper-Scissors!")

print(choice)