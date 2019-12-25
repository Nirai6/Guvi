#POWER OF A NUMBER
n=int(input("Enter a number"))
p=int(input("enter power"))
powers=1
for i in range (0,p) :
    powers=powers*n
print("The power is ",powers)
