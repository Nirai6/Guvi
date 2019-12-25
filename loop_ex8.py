#MULTIPLICATION TABLE
n=int(input("Enter number for multiplication table"))
a=int(input("Enter how many times"))
for i in range(1,a+1):
  m=n*i
  print(n,"*",i,"=",m)
  i=i+1
