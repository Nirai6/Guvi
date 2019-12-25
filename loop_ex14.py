#PRODUCT OF DIGITS OF NUMBER
n=int(input("Enter any number"))
mul=1
while n>0:
    d=n%10
    n=n//10
    mul=mul*d
print(mul)

    

         
