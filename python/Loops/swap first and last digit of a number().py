#Swap first and last digit of a number
n=int(input("Enter number"))
t1=n
t2=n
t3=n
count=0
while t1>10:
    t1=t1//10
    count+=1
p=1
for i in range(1,count+1):
    p=p*10
p=pow(10,count)

while t2>10:
     t2=t2%10
l1=(n-t2)+t1
l2=l1-p
l3=p*t2
l4=l3+l2
print(l4)
