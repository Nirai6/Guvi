#FIBONACCI SERIES
n=int(input("enter a number"))
n1=0
n2=1
count=0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
    while count<n:
        print("Fibonacci sequence are")
        print(n1)
        nt=n1+n2
        n1=n2
        n2=nt
        count+=1
        
        
