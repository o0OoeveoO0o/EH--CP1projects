#EH Escape room p1
import time
print("Welcome to Monochromania")
print("As you can see everything is black and white. you just need to escape :D")
time.sleep(.1)
print("...")
time.sleep(.2)
print("RAAAWr *The entire room shakes*")
time.sleep(.1)
print("Oh yeah there is a monster looking for you")
print("Everytime you get the wrong answer an alarm will sound")
print("Hear the steps maybe he's close maybe he's away.")


paswrd = ("Kitty tamer of unicorns")

while True:
    while True:
        try:
            guess = int(input("Guess the password: "))
            
        if guess  == paswrd:
            print("The alarm doesn't sound and the door opens...RUN!! *You hear the monster's steps coming for you* when you cross the door you are in your bed...it was...all a dream......or not?")
