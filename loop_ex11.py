#SUM OF FIIRST AND LAST DIGIT OF A NUMBER
n=int(input("Enter any number"))
a=n
while n>10:
    n=n//10
while a>10:
    a=a%10
sum=a+n
print("The sum is",sum)
          
