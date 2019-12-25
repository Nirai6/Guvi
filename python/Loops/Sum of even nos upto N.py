#SUM OF ODD NOS UPTO N
n=int(input("Enter"))
sum=0
for i in range(1,n):
 if(i%2!=0):
  sum=sum+i
print(sum)
