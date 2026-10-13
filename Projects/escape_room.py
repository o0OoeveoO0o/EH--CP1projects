#EH Escape room p1
import time
print("Welcome to Monochromania")
print("As you can see everything is black and white. you just need to escape :D")
time.sleep(2)
print("...")
time.sleep(.1)
print("RAAAWr *The entire room shakes*")
time.sleep(1)
print("Oh yeah there is a monster looking for you")
print("Everytime you get the wrong answer an alarm will sound")
print("Hear the steps maybe he's close maybe he's away.")

paswrd = ("Kitty tamer of unicorns")

while True:
    while True:
        try:
            passd = int(input("Insert the password: "))
            if passd == False:
                print("That's not the password The alarm sounds you hear the monster coming for you* ")
                continue
            break
        except:

            if passd == paswrd:
                print("*The alarm goes off and the door opens* You escaped")
        break
    
    print("The alarm sounds the mosnter is getting closer")
