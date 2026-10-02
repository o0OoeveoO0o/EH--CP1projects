

age = 17
licese = false
if age >= 18: #<-- all conditionals starts with an if
    print("You're an adult and can vote!")
elif age >= 15 and licese:#<- in between
    print("You can drive, but you're a minor go to school>:(")
elif age >= 15 and not license:
    print("You could drive but u need to do the paperwork")
else: #<--marks the end of the condition
    print("you're a minor. Go to school")


win = True
hp = 25

if win or hp < 1:
    print("Game over")
    if hp >0:
        pass
    else:
        print ("gg's")
else:
    print("the game still going")