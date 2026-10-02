#Evans Hidalgo p1 dice roller1
import random

d4 = random.randint(1, 4)
d6 = random.randint(1,6)
d8 = random.randint(1,8)
d10 = random. randint(1,10)
d12 =random.randint(1,12)
d20 = random.randint(1,20)

def roll():
    dice = input("what type of dice you want to roll D :").strip()

    if dice == "4":
        print("Your rolled " , d4)
    elif dice == "6":
        print("Your rolled " , d6)
    elif dice == "8":
        print("Your rolled " , d8)
    elif dice == "10":
        print("Your rolled " , d10)
    elif dice == "12":
        print("You rolled " , d12)
    elif dice == "20":
        print("Your rolled " , d20)
    else:
        print("invalid input: please try again")
        roll()

roll()