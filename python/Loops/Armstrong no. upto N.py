#ARMSTRONG NUMBER UPTO N
r=int(input("Enter range"))
for n in range(0,r+1):
    t=n
    sum=0
    while n>0:
        r=n%10
    
        a=r*r*r
    
        sum+=a
        n=n//10
   
    if(t==sum):
         print("Armstrong numbers are"sum)
        
   
