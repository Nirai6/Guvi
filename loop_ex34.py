#DECIMAL TO BINARY
dec=int(input("enter decimal number"))
print("The decimal value of", dec, "is:")
print(bin(dec).replace("0b", ""), "in binary.")
