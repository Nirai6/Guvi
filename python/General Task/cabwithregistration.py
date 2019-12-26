print("Welcome to Devil Cab Service")
o=0
r=0
Registereduser={
 'user1':'pass1',
 'user2':'pass2',
 'user3':'pass3'
}
b=0
f4=4
while b<4:
    f=str(input("Enter registered or notregistered: "))
    f=f.upper()
    if (f=="REGISTERED"):
        getUsernmae = str(input("Enter User name: "))
        getPassword = str(input("Enter Password: "))
        if (getUsernmae,getPassword) in Registereduser.items():
            print("valid")
            r=r+1
            
        else:
            print("Sorry you are not registerd")
            break
            
        
        
        
    if (f=="NOTRREGISTERED"):
        getUsernmae = str(input("Enter new User name: "))
        getPassword = str(input("Enter Password: "))
        Registereduser.__setitem__(getUsernmae, getPassword)
        if (getUsernmae,getPassword) in Registereduser.items():
            print("Registration sucessfull")
            r=r+1
    else:
        #print("enter valid")
        #print("you have",f4-1,"attempt left: ")
        b+=1
        f4-=1
    
    if(r==1):
            Source = 0
            geDestination = int(input("Enter destination in km: "))
            distance = geDestination
            if distance>5:
                print("******If the distance is greter than 5km price may increase according to car type*******")
            count=0
            c=3
            while count<3:
                print("\n1-->Mini","\n2-->Sedan","\n3-->xuv","\n4-->prime")
                a=str(input("Enter vehicle: "))
                a=a.upper()
    
                if (a=="MINI"):
                    print(a)
                    count1=0
                    c1=3
                    while count1<3:
                        print("\n1-->Santro","\n2-->beat","\n3-->nano","\n4-->indica")
                        a1=str(input("Enter model: "))
                        l=a1
                        a1=a1.upper()
                        if distance<=5:
                            price=5
                            Total=price * distance
                            print(Total)
                        else:
                            edistance=distance-5
                            mprice=5
                            mtotal=5*mprice
                            eprice = 10
                            eTotal = eprice * edistance
                            Total=eTotal+mtotal
                            print(Total)
                        if (a1=="SANTRO"):
                            print(a1)
                            break
                        if (a1=="BEAT"):
                            print(a1)
                            break
                        if (a1=="NANO"):
                            print(a1)
                            break
                        if (a1=="INDICA"):
                            print(a1)
                            break
                        else:
                            print("you have",c1-1,"attempt left... ")
                            count1=count1+1
                            c1=c1-1
                    break
                if (a=="SEDAN"):
                    print(a)
                    count2=0
                    c2=3
                    while count2<3:
                        print("\n1-->Hondacity","\n2-->hondacivic","\n3-->swiftdizire","\n4-->cruze")
                        a2=str(input("Enter model: "))
                        a2=a2.upper()
                        l=a2
                        if distance<=5:
                            price=10
                            Total=price * distance
                            print(Total)
                        else:
                            edistance=distance-5
                            mprice=10
                            mtotal=5*mprice
                            eprice = 30
                            eTotal = eprice * edistance
                            Total=eTotal+mtotal
                            print(Total)
                        if (a2=="HONDACITY"):
                            print(a2)
                            break
                        if (a2=="HONDACIVIC"):
                            print(a2)
                            break
                        if (a2=="SWIFTDIZIRE"):
                            print(a2)
                            break
                        if (a2=="CRUZE"):
                            print(a2)
                            break
                        else:
                            print("you have",c2-1,"attempt left: ")
                            count2=count2+1
                            c2=c2-1
                    break
                if (a=="XUV"):
                    print(a)
                    count3=0
                    c3=3
                    while count3<3:
                        print("\n1-->Bolero","\n2-->Scorpio","\n3-->Tavera","\n4-->Breeza")
                        a3=str(input("Enter model: "))
                        a3=a3.upper()
                        l=a3
                        if distance<=5:
                            price=30
                            Total=price * distance
                            print(Total)
                        else:
                            edistance=distance-5
                            mprice=30
                            mtotal=5*mprice
                            eprice = 50
                            eTotal = eprice * edistance
                            Total=eTotal+mtotal
                            print(Total)
                        if (a3=="BOLERO"):
                            print(a3)
                            break
                        if (a3=="SCORPIO"):
                            print(a3)
                            break
                        if (a3=="TAVERA"):
                             print(a3)
                             break
                        if (a3=="BREEZA"):
                            print(a3)
                            break
                        else:
                            print("you have",c3-1,"attempt left: ")
                            count3=count3+1
                            c3=c3-1
                    break
                if (a=="PRIME"):
                    print(a)
                    count4=0
                    c4=3
                    while count4<3:
                        print("\n1-->Benz","\n2-->audi","\n3-->bmw","\n4-->RollsRoyce")
                        a4=str(input("Enter model: "))
                        a4=a4.upper()
                        l=a4
                        if distance<=5:
                            price=50
                            Total=price * distance
                            print(Total)
                        else:
                            edistance=distance-5
                            mprice=50
                            mtotal=5*mprice
                            eprice = 100
                            eTotal = eprice * edistance
                            Total=eTotal+mtotal
                            print(Total)
                        if (a4=="BENZ"):
                            print(a4)
                            break
                        if (a4=="AUDI"):
                            print(a4)
                            break
                        if (a4=="BMW"):
                            print(a4)
                            break
                        if (a4=="ROLLSROYCE"):
                            print(a4)
                            break
                        else:
                            print("you have",c4-1,"attempt left: ")
                            count4=count4+1
                            c4=c4-1
                    break
                else:
                    print("you have",c-1,"attempt: ")
                    count=count+1
                    c=c-1
                          #BILL CODE
            print("*******Bill Recipt*******")
            print("Welcome", getUsernmae)
            print("Total distance is", distance,"km")
            print("Your car type is", a)
            print("Your car model is", l)
            print("Total cost is", Total,"₹")
            print("Thank u for choosing us")
        
