import random

def play():
    user = input("Choose: Rock (R), Paper (P), or Scissors(S)? ")
    computer = random.choice(["R", "P", "S"]) 

    if user.upper() == computer:
        return f"We both chose {computer}! It's a tie."

    if is_win(user, computer): #user is player vs computer
        return f"You won! {user.upper()} beats {computer}!"
    
    return f"Sorry! {computer} beats {user.upper()}. You lost." # do not need if statement before this. returns only if computer won.

#Rules for winning: R > S, P > R, S > P

def is_win(player, computer):
    #return true if player wins
    if (player.upper() == "R" and computer == "S") or (player.upper() == "P" and computer == "R") or (player.upper() == "S" and computer == "P"):
        return True

print(play())
