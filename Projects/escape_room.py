# EH Escape room p1

import time

print("Welcome to Monochromania")
print("As you can see everything is black and white. You just need to escape :D")
time.sleep(2)
print("...")
time.sleep(0.5)
print("RAAAWr *The entire room shakes*")
time.sleep(1)
print("Oh yeah, there is a monster looking for you.")
print("Every time you get the wrong answer an alarm will sound.")
print("Hear the steps... maybe he's close, maybe he's away.")
print("You only have 3 attempts before the monster finds you!")
print()

password = "Kitty tamer of unicorns"
attempts = 0
max_attempts = 3
escaped = False

hints = [
    "Hint 1: Imagine a feline animal riding a horse...",
    "Hint 2: Think of a feline that controls a mystical animal...",
    "Hint 3: The password is 'Kitty tamer of unicorns'... wait, did I just say that?!"
]

while attempts < max_attempts:
    user_input = input("Insert the password: ")
    attempts += 1

    if user_input == password:
        escaped = True
        break
    else:
        remaining = max_attempts - attempts
        print("That's not the password! *The alarm sounds* You hear the monster coming for you...")
        print(hints[attempts - 1])
        if remaining > 0:
            print(f"The alarm keeps ringing... the monster is getting closer! ({remaining} attempt(s) left)\n")
        else:
            print("You hear heavy footsteps right behind you...")

if escaped:
    print("*The alarm stops and the door opens*")
    print("*** Congratulations! You escaped Monochromania! ***")
    print("You are free!")
else:
    print()
    print("RAAAAWR!!!!")
    time.sleep(1)
    print("*The monster jumps on you*")
    print("You have been DEVOURED by the monster...")
    print("GAME OVER")
