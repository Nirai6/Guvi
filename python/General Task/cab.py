userName = "Nirai"
Password = "pro"
i = 0
while i < 4:
    getUsernmae = str(input("Enter User name"))
    getPassword = str(input("Enter Password"))
    if (userName == getUsernmae):
        if (Password == getPassword):
            Source = 0
            geDestination = int(input("Enter destination"))
            distance = geDestination
            if distance>5:
                print("******If the distance is greter than 5km price may increase according to car type*******")
            print("Select any model from below ")
            car = {1: 'Mini', 2: 'Sedan', 3: 'XUV', 4: 'premium'}
            c = int(input("Select your car 1 -->Mini 2 --> Sedan 3 -->XUV 4 -->premium "))
            cars=car.get(c)
            if cars:
                if car[c] == 'Mini':
                    model = {1: 'INDICA', 2: 'BEAT', 3: 'SANTRO', 4: 'I10 '}
                    m = input("Select your car 1 -->INDICA 2 --> BEAT 3 -->SANTRO 4 -->I10 ")
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

                if car[c] == 'Sedan':
                    model = {1: 'CRUZE', 2: 'I20', 3: 'DZIRE', 4: 'SWIFT '}
                    m = int(input("Select your car 1 -->CRUZE 2 --> I20 3 -->DZIRE 4 -->SWIFT "))
                    if distance<=5:
                        price=10
                        Total=price * distance
                        print(Total)
                    else:
                        pedistance=distance-5
                        mprice=10
                        mtotal=5*mprice
                        eprice = 30
                        eTotal = eprice * edistance
                        Total=eTotal+mtotal
                        print(Total)

                if car[c] == 'XUV':
                    model = {1: 'SCORPIO', 2: 'BOLERO', 3: 'TAVERA', 4: 'BREEZA '}
                    m = int(input("Select your car 1 -->SCORPIO 2 --> BOLERO 3 -->TAVERA 4 -->BREEZA "))
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
                        
                if car[c] == 'premium':
                    model = {1: 'BMW', 2: 'AUDI', 3: 'MASSERATI', 4: 'BENZ '}
                    m = int(input("Select your car 1 -->BMW 2 --> AUDI 3 -->MASSERATI 4 -->BENZ "))
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
            else:    
                print("Wrong selection")
                
                
            print("*******Bill Recipt*******")
            print("Welcome", userName)
            print("Total distance is", distance,"km")
            print("Your car type is", car[c])
            print("Total cost is", Total)
            print("Thank u for choosing us")


            break
        else:
            print("Password is wrong")
    else:
        print("userName is wrong")
else:
    print("try again")
    i = i + 1
