userName="Nirai"
Password="pro"
i=0
while i<4:
 getUsernmae=str(input("Enter User name"))
 getPassword=str(input("Enter Password"))
 if (userName==getUsernmae):
    if(Password==getPassword):
       Source=0
       geDestination=int(input("Enter destination"))
       distance=geDestination
       print("Select any model from below ")
       car= {1: 'Mini', 2: 'Sedan', 3: 'XUV',4:'premium'} 
       c=int(input("Select your car 1 -->Mini 2 --> Sedan 3 -->XUV 4 -->premium ")) 
       cars=car.get(c)
       if cars:
        if car[c]=='Mini':
         model= {1: 'INDICA', 2: 'BEAT', 3: 'SANTRO',4:'I10 '}
         m=input("Select your car 1 -->INDICA 2 --> BEAT 3 -->SANTRO 4 -->I10 ")
         price=10
         Total=price*distance
         print(Total)
       
        if car[c]=='Sedan':
         model= {1: 'CRUZE', 2: 'I20', 3: 'DZIRE',4:'SWIFT '}
         m=int(input("Select your car 1 -->CRUZE 2 --> I20 3 -->DZIRE 4 -->SWIFT "))
         price=30
         Total=price*distance
         print(Total)

       
        if car[c]=='XUV':
         model= {1: 'SCORPIO', 2: 'BOLERO', 3: 'TAVERA',4:'BREEZA '}
         m=int(input("Select your car 1 -->SCORPIO 2 --> BOLERO 3 -->TAVERA 4 -->BREEZA "))
         price=50
         Total=price*distance
         print(Total)

        if car[c]=='premium':
         model= {1: 'BMW', 2: 'AUDI', 3: 'MASSERATI',4:'BENZ '}
         m=int(input("Select your car 1 -->BMW 2 --> AUDI 3 -->MASSERATI 4 -->BENZ "))
         price=100
         Total=price*distance
       else:
        print("wrong")
      
        print("*******Bill Recipt*******")
        print("Welcome",userName)
        print("Total distance is",distance)
        print("Your car type is",car[c] )
        print("Total cost is",Total)
        print("Thank u for choosing us")
       break
    else :
     print("Password is wrong")
 else:   
      print("userName is wrong")
else:
  print("try again")
  i=i+1