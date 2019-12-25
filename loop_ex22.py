#GCD
n=int(input("Enter a number"))
a=int(input("Enter a number"))
if n>a:
    smaller=a
    
else:
    smaller=n
 
for i in range(1,smaller+1):
    if (n%i==0)and(a%i==0):
        gcd=i
print("gcd is",gcd)
