# Gino, make me rock paper scissors!
import random

print("Welcome to Rock Paper Scissors!")

playerSelection = input("Type in rock, paper, or scissors. ")

# Gino, we are going to generate a random number in order
# to make the computers selection.

randomNumber = random.randint(1, 3)
if randomNumber == 1:
    computerSelection = "rock"
elif randomNumber == 2:
    computerSelection = "paper"
elif randomNumber == 3:
    computerSelection = "scissors"

print("Player throws: " + playerSelection)
print("Computer throws: " + computerSelection)
