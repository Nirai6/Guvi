#LCM
n=int(input("Enter a number"))
a=int(input("Enter a number"))
if n>a:
   greater=n
    
else:
    greater=a
 
while(True):
    if (greater%n==0) and (greater%a==0):
        print("LCM IS",greater)
        break
    greater=greater+1
        
