#VL While Loops

import random
import time

goose = random.randint(1,20)
Duck = 1 #<- start point

while goose > Duck: #Whiles is the key word for a while loop | goose > Duck are the end point
    print("duck...")
    time.sleep(0.1)
    Duck += 1#<-This is the incrimentor used to change the iterator
print("GOOSE!!")
#iterator keeps track of the current iteration of our loop

count = 1 
while count <= 30:
    print(count)
    time.sleep(.1)
    count += 1


number = random.randint(1,101)

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess <0 or guess > 100:
                print("U should read the instructions")
                continue
            break
        except:
            print("that is not a number")

    if guess == number:
        print("U win")
        break
    elif guess < number:
        print("That is too low ")
    elif guess > number:
        print("That number is too high ")
    else:
        print 




import random
import time

goose = random.randint(1,20)
Duck = 1 #<- start point

while goose > Duck: #Whiles is the key word for a while loop | goose > Duck are the end point
    print("duck...")
    time.sleep(0.1)
    Duck += 1

    if Duck == 15:
        print("game over")
        break

else:
    print("GOOSe!")