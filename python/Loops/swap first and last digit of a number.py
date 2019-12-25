n = int(input("Enter the number:"))
t1 = n
t2 = n
count = 0
while n> 0:
    n = n//10
    count += 1
d = count - 1    
a = t1 % 10
b = t1 // (10 ** d)
t1 = t1 - (b*(10**d)) - a
t1= t1 + (a*(10**d)) +b
print("The first and last digit of the number ",t2,"is swapped as",t1)
