# snake water gun game

import random
comp = random.randint(0,2)

user = int(input("Enter 0 for Snake , 1 for Water and 2 for Gun: "))

def check (comp,user):
    if comp == 0 and user == 1:
        print(f"computer choses : {comp}")
        print(f"You choses : {user}")
        print("Snake beats Water" "\n" "you lose")
    elif comp == 1 and user == 2:
        print(f"computer choses : {comp}")
        print(f"You choses : {user}")
        print("Water beats Gun" "\n" "you lose")
    elif comp == 2 and user == 0:
        print(f"computer choses : {comp}")
        print(f"You choses : {user}")
        print("Gun beats Snake" "\n" "you lose")
    elif user == 0 and comp == 1:
        print(f"computer choses : {comp}")
        print(f"You choses : {user}")
        print("Snake beats Water" "\n" "you lose")
    elif user == 1 and comp == 2:
        print(f"computer choses : {comp}")
        print(f"You choses : {user}")
        print("Water beats Gun" "\n" "you lose")
    elif user == 2 and comp == 0:
        print(f"computer choses : {comp}")
        print(f"You choses : {user}")
        print("Gun beats Snake" "\n" "you lose")
    else:
        print("Both are same" "\n" "Its a Draw")

check(comp,user)
