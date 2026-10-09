#EH p1 factorial calculator
import math
while True:
    try:
        numBR = int(input("What number do you want the factorial of: "))
        if numBR < 0:
            print("Please enter a non-negative integer.")
            continue
        
        if numBR == 0:
            print("0 = 1")
        else:
            expr = " × ".join(str(i) for i in range(numBR, 0, -1))
        rest = (math.factorial(numBR)) 
        print(f"{expr} = {rest}")
            
    except ValueError:
        print("Invalid :P. Please enter an integer>:P ")
        continue
      
    again = input("\nDo you want to try again??: ").lower()
    if again != 'y':
        break
