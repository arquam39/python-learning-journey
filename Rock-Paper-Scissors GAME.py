import random

# Mapping numbers to names for better readability
options = {0: "Rock", 1: "Paper", 2: "Scissors"}

comp = random.randint(0, 2)
user = int(input("Enter 0 for Rock, 1 for Paper, and 2 for Scissors: "))

def check(comp, user):
    # Validate input
    if user not in [0, 1, 2]:
        print("Invalid input! Please choose 0, 1, or 2.")
        return

    print(f"Computer chose: {options[comp]}")
    print(f"You chose: {options[user]}")

    # Logic Check
    if comp == user:
        print("It's a Draw!")
    
    # Winning conditions for the user
    elif (user == 0 and comp == 2) or \
         (user == 1 and comp == 0) or \
         (user == 2 and comp == 1):
        print(f"{options[user]} beats {options[comp]}! You Win! 🎉")
    
    # If it's not a draw and you didn't win, you lost
    else:
        print(f"{options[comp]} beats {options[user]}! You Lose. 💀")

check(comp, user)
