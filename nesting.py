#Notes WASA
win= True
text= False

if win:
    if text:
        print("Hallalujah")
    else:
        print("Try Again")
else:
    print("You failed")
names=["Batman TDK", "CAS Superman", "Cosmic Ghost Rider", "Wally west Dr Manhattan", "TOBA Hulk" , "The Living tribunal"]

while True:
    for name in names:
        print(f"{name} The presence")
    again = input("Do you need to see them again?: ")
    if again.lower() == "yes":
            pass
    else:
         break