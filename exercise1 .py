a= []
n = int(input("Enter the list size"))
for i in range(0, n):
    item = int(input())
    a.append(item)
print(a)
count=0 
count1=0
j,k=0,0
for i in a:
 if (i==7) : 
   count=count+1
   print("position of 7 is at",j)
 if (i==2)  : 
    count1=count1+1
    print("position of 2 is at ",k)
 j=j+1
 k=k+1
if(count>0):
    print("Element 7 exist and count is",count)
else:
    print("element 7 not exist")
if(count1>0):
    print("Element 2 exist and count is ",count1)
else:
    print("element 2 not exist")
 


    

    