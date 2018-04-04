import random

secret = random.randint(1,10)
guess = 0
    
print("welcome")
print("I have a number")
print("here is a number from 1 to 10")

while guess != secret :
    guess = int(input("what is your guess?  "))
    
    if guess < secret:
        print ('too low')
    if guess > secret:
        print ('too high')
        
if guess ==secret:
    print ("you got it")
    
guess_flag=input("do you want to continue(Y/N): ")
if guess_flag=="Y":
    guess()
