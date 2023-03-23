import random
num=random.randint(1,100)
score=100
print ("The number is between 1 and 100")
while True :
    inp=int(input("What is your guess : "))
    if num==inp:
        print ("Congrats you guessed it correctly!")
        print (f"Your final score is {score:.1f}")
        exit()
    elif inp>num:
        print ("Number is smaller")
        score=0.9*score
    else :
        print ("Number is greater")
        score=0.9*score