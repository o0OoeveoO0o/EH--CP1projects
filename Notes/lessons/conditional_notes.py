#EH Conditional notes

grade =70

if grade >= 90:
    print("GREAT JOB")
elif grade >= 70:
    print("You're passing!!")
if grade >= 70: #If starts every conditional| Grade >= this is our boolean statement| In the boolean statement there is a : named colon which leads to the fact that the next part meeds to be...  
    print("You're passing!!")
#** the bllank part Indent
else:#<- else = any other instance
    print("You'll do it better the next time don't worry")
    print("You can do it just study more")

username = input("Instert a username: ")
if bool(username):
    print("You didn't type it in")
elif username == "Mrpapeador67":
    print("Hello Mrpapeador67")
else:
    print("you're not Mrpapeador67 DIEEE!!")

raining = False

if raining:
    print("It is raining over the city")
else:
    print("I hope it rains")