#EH p1 what is my grade

perce = float(input("What is your grade percentage: "))
if perce >= 93:
        lett = "A"
elif perce >= 90:
        lett = "A-"
elif perce >= 87:
        lett = "B+"
elif perce >= 83:
        lett = "B"
elif perce >= 80:
        lett = "B-"
elif perce >= 77:
        lett = "C+"
elif perce >= 73:
        lett = "C"
elif perce >= 70:
        lett = "C-"
elif perce >= 67:
        lett = "D+"
elif perce >= 63:
        lett = "D"
elif perce >= 60:
        lett = "D-"
else:
        lett = "F"

print(f"Your grade is {perce}% which is a {lett}")
