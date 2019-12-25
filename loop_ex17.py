#FREQUENCY OF DIGIT IN A NUMBER
n=int(input("enter any nuymber"))
d=int(input("enter number to find frequency"))
temp=n
count=0
reverse=0
while temp>0:
    remainder=temp%10
    if remainder==d:
        count=count+1
    temp=temp//10
print("the number ",d,"is repeated ",count,"times")    
