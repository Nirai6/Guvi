a= []
n = int(input("Enter the list size"))
for i in range(0, n):
    item = int(input())
    a.append(item)
print(a)
for x in a:
    l=1
    count=0
    for j in range(x):
     if (x%l==0):
      count+=1
     l+=1
    if(count==2):
         print(x,"is a prime number")
    else:
         print(x,"is  a composite number")

    

    