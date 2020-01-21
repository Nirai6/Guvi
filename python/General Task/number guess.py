from random import randint
n=randint(0,9)
i=0
while(i<5):
    a=int(input("guess number"))
    if a == n:
        print("Guess is correct",n)
        break
    else:
        print("Wrong guess")
        print("Number of attempt remaining is ",4-i)
    i=i+1
