#Guess the number
#abhinaba bala  8.1.17

import random

print ("hi, this is a guess the number game,\n you will have to guess it within the range 1 to 120 in minimum amount of steps\n")

while True:
    N = random.randint(1,120)
    
    count = 1

    while True:
        ask = int(input("So what's your guess number"))
      #  if (type(ask) != int):
            
        if (N==ask):
            print ("good job, you have reached the goal in ", count, "steps")
            break
        if (N< ask):
            print ("the input is larger than the number...try again")
            count += 1
        if (N>ask):
            print ("the inputed number is lesser than the target, think bigger!!")
            count += 1
        for s in range(80):
            print ("-", end='')

    cont = str(input("wanna continue with a new number, enter Y "))
    if cont!=("Y"and"y"):
        break


print ("Nice playing with you")
