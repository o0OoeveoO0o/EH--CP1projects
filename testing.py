#EH User Sign-in

username = ("Random_username61")
password = ("rAnDooM_PaSsWoRd")
def roll():
    usnam = input("What is the username? ")
    passcode = input("what is the password? ")

    if usnam == "Random_username61":
        print("User name = " + username)
    if passcode == "rAnDooM_PaSsWoRd":
        print("User password = " + password)
    elif usnam == False:
        print("Try again")
    elif passcode == False:
        print("Please try gain")
    else:
        print("YOU ARE NOT Random_username61 check the password or username please!!!")

        roll()
roll()