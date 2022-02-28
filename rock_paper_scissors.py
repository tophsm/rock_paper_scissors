#Project 4
import random

def play():
    user = input("Choose: Rock (R), Paper (P), or Scissors(S)? ")
    computer = random.choice(["R", "P", "S"]) 

    if user == computer:
        return "It's a tie."

    if is_win(user, computer): #user is player and computer is opponent
        return "You won!"
    
    return "Sorry! You lost." # do not need if statement before this. returns only if computer won.

#Rules for winning: R > S, P > R, S > P

def is_win(player, opponent):
    #return true if player wins
    if (player == "R" and opponent == "S") or (player == "P" and opponent == "R") or \
        (player == "S" and opponent == "P"):
        return True

print(play())
