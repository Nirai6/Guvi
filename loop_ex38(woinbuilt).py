#BINARY TO DECIMAL
import math
n = int(input("Enter the binary number : "))
decimal = 0
remainder = 0
count = 0
while (n!=0):
    remainder = n%10
    n = int(n / 10)
    decimal = decimal + remainder*math.pow(2,count)
    count = count + 1
print("Decimal Number : ",int(decimal))