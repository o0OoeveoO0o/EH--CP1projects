#functions notes

name = input("Tell me your name: ")
def birthday(name , age= 35):#def= define,| name , age = parameters
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you")
    print(f"You are now {age} years old")


print("November")
birthday("Tia", 30)
print("December")
birthday("Xavier", 24)
print("January")
birthday("Teryson", 20)
birthday(name)
birthday()
attempts = 0
def increase():
    return attempts + 1

def stupid_proof(user_answer, correct):
        user_answer = user_answer.strip().title()
        if user_answer in correct:
            return True , user_answer , increase()
        else:
            return False , user_answer , increase()
while True:
    capital = input("What us the capital of Utah? ")
    correct, capital, attempts = stupid_proof(capital, ["Salt Lake City" , "SLC" , "Salt Lake" ] )
    if correct:
        print(f"Good job {capital} is the capital of Utah!")
        break
    else:
        print(f"Try again, {capital} is not the capital of Utah. You have tried {attempts} times")