# EH Mapping notes
import math
def times (number):
    return number *2

numbers = range(1,6)

multiply_members = map(times,numbers)# in map(times,numbers) times = function and  numbres = list
print(list(multiply_members))
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)

siblings =["Alex", "Katie" , "Andrew" , "Tia","Treyson", "Xavier","Jake"]

lenght= list(map(len, siblings))
print(lenght)

print(math.factorial(5))
