#DECIMAL TO BINARY
n = int(input("Enter the decimal number : "))
binary = 0
i = 1
while(n != 0):
    remainder = n % 2
    n = int(n //2)
    binary = binary+remainder * i
    i = i * 10
print("Equivalent binary number : ",binary)
