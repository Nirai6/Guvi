#ARMSTRONG NUMBER OR NOT
n=int(input("enter the value"))
t=n
sum=0
while n>0:
    r=n%10
    
    a=r*r*r
    
    sum+=a
    n=n//10
print(sum)
if(t==sum):
    print("armstrong number")
else:
    print("not")
