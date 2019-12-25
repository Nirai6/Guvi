#PRIME NUMBER UPTO N
num=int(input("enter the value"))
print("prime nos. are")
for val in range (1, num + 1):
    
    
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val)
                
