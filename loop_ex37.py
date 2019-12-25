#SUM OF PRIME NOS. UPTO N
n=int(input("Enter number"))
sum=0
for i in range(1,n+1):
    if n==1:
        print(1)
    else:
        for n in range(2,i):
            if(i%n==0):
                break
        else:
             
         sum=sum+i
         
print(sum)