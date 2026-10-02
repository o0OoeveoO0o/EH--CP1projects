#EH period 1 what is my grade

grade = input("What is your grade? ")

def roll():
    if grade >= 93:
        print(f"{grade} + !! that's an A. That's PERFECT keep working!! ")
    elif grade >= 89:
        print(grade + "!! that's an A-. That's okey you got this!! ")
    elif grade >=87:
        print(grade + " that's a B+ ;) you can do it")
    else: 
        print("You have a F you're not passing")
        roll()

roll()