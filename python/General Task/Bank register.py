dataBase={}
b=open("dic.txt","w+")
def register():
    import random
    import getpass
    c=0
    while(c<3):
        email=input("Enter ur email")
        if "@gmail.com" in  email:
            if email=='@gmail.com':
                print("Try again")
                c=c+1
            else:
                print("email is",email)
        

                break
        else:
            print("Try agan")
            c=c+1
    AccNo = list(range(1000,9999))
    Name=input("Enter user name")
    random.shuffle(AccNo)
    a=AccNo.pop()
    print("AccNo is ",a)
    
    password=getpass.getpass("Enter pass")
    dataBase.update({a:[Name,email,password]})
    
    print(dataBase)
  

def login():
    a1=int(input("Enter ur account no."))
    p1=input("Enter ur password")
    key,value=a1,p1
    if key in dataBase and value in dataBase[key]:
        print("valid")
    else:
        print("iilegal entry")
register()
register()

login()
  
