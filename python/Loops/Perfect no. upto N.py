#PERFECT NUMBER UPTO N
r=int(input("Enter range"))
for n in range (1,r+1):
    sum=0
    for i in range (1,n):
        if(n%i)==0:
        
            sum=sum+i
    if sum==n:
        print(n)
    
   
