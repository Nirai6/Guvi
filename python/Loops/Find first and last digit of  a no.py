#FIND FIRST AND LAST DIGIT OF A NUMBER
n=int(input("Enter any number"))
a=n
while n>10:
    n=n//10
print("The first digit is ",n)
while a>10:
    a=a%10
print("The last digit is ",a)
          
