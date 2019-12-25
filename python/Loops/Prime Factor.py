#PRIME FACTOR
n=int(input("enter number"))
print("The prime factors of",n,"are")
for i in range(1,n+1):
    for a in range(2,i):
        if(i%a)==0:
            break
    else:
       
        c=[]
        c.append(i)
        for m in c:
            
            if(n%m)==0:
                print(m)
    

