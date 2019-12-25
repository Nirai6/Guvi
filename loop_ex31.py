#STRONG NUMBER UPTO N
p=int(input("enter range"))
for n in range(1,p+1):
    t=n
    sum=0
    while(t>0):
        fact=1
    
        r=t%10
        for i in range(1,r+1):
            fact=fact*i
    
        t=t//10
        sum=sum+fact
        
    if sum==n:
        print(sum)
    

    
