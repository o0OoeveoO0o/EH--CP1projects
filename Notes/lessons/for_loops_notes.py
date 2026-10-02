#EH For loops notes
import time


# Iteration 
siblings = ["Alex", "Katie" , "Andrew" , "Tia","Treyson", "Xavier","Jake"]

for sibling in siblings:# for key board for for loop| siblings is the interater variable| sibling I, X or a single version of a list| siblings : name of the list
    print(f"Good Morning {sibling}!")

grades = [100, 87 , 53 , 45 , 78 , 72 , 88 , 3 , 94]
average = 0

for grade in grades:
    average += grade 
    print(f"{grade} was added")
average = average/len(grades)
print(f"The average grade is {average:.2f}")

for i in range(2,21,2): # 2 is the number where it starts, 21 is the number wher it stops ,and 2 in the othe side is the iterator (the number you use to count like 2,4,6,8,10) <- a boolean
    print(i)
    time.sleep(0.5)

for i in range(20, 0, -1):
    print(i)
    time.sleep(0.5)

    if i == 12:
        print('Wait it is lunch time')
        break