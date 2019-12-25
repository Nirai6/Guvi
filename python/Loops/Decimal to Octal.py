#DECIMAL TO OCTAL
n = int(input("Enter the decimal number : "))
octal = 0
i = 1
while(n != 0):
    remainder = n % 8
    n = int(n //8)
    octal = octal+remainder * i
    i = i * 10
print("Equivalent octal number : ",octal)