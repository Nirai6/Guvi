import random
import getpass
import os
import sys
dataBase={}
authenticator={}
authfile=open("authenticator.txt","a+")
file=open("dataBase.txt","a+")
if(os.path.getsize("dataBase.txt")==0):
    print()
else:
    file=open("dataBase.txt","r")
    dataBase=eval(file.read())
    file.close()
    authfile=open("authenticator.txt","r")
    authenticator=eval(authfile.read())
    authfile.close()
print("-----------------------------------------------------------------Welcome to Devil Bnking---------------------------------------------------------------")    
    
def main_Menu(a1):
    k=0
    temp_Balance=dataBase[a1][4]["Balance"]
    while(k<3):
        if temp_Balance<1000:
            print("Welcome new user enter minimum of 1000 to bank account to proceed")
            temp_Balance=int(input("Enter money to deposit : "))
            if temp_Balance>999:
                dataBase[a1][4]['Balance']=temp_Balance
                file=open("dataBase.txt","w")
                file.write(str(dataBase))
                file.close()
                break
            else:
                print("low balnce\r")
                k=k+1
                print("only",3-k,"chance remaing after excluding the chance program will be terminated")
                if k==3:
                    sys.exit()
        else:
            break
    print("""1--->Balance
2--->Withdraw
3--->deposit
4--->History
5--->exit""")
    choice=int(input("Enter ur choice for main_Menu : "))
    while (choice>0 and choice<4):
        if choice==1:
            print(dataBase[a1][4]["Balance"])
            choice=int(input("Enter ur choice for main_Menu :"))
        if choice==2:
            Balance=int(input("Enter money to withdraw :"))
            temp_Balance=dataBase[a1][4]["Balance"]
            if Balance>temp_Balance:
                print("Insufficient fund")
            elif temp_Balance-Balance<1000:
                print("Minimum balance of 1000 must be maintained!!!")
            if Balance<temp_Balance and temp_Balance-Balance>1000:
                rem_Balance=temp_Balance-Balance
                print("Ammount withdrawn is %d"%(Balance))
                print("Balance is %d"%(rem_Balance))
                dataBase[a1][4]['Balance']=temp_Balance-Balance
                dataBase[a1][4]['Withdraw'].append(str(Balance)+",")
                dataBase[a1][4]['History'].append("-"+str(Balance))
                choice=int(input("Enter ur choice for main_Menu :"))
        if choice==3:
            Balance=int(input("Enter money to deposit : "))
            temp_Balance=dataBase[a1][4]["Balance"]
            rem_Balance=temp_Balance+Balance
            print("Ammount deposited is %d"%(Balance))
            print("Balance is%d"%(rem_Balance))
            dataBase[a1][4]['Balance']=temp_Balance+Balance
            dataBase[a1][4]['Deposit'].append(str(Balance)+",")
            dataBase[a1][4]['History'].append("+"+str(Balance))
            choice=int(input("Enter ur choice for main_Menu :"))
        if choice==4:
            print(dataBase[a1][4]["History"])
            choice=int(input("Enter ur choice for main_Menu :"))
        if choice==5:
            file=open("dataBase.txt","w")
            file.write(str(dataBase))
            file.close()
            print("You are being redirected to Registration page : ")
            break
    

def register():
        file=open("dataBase.txt","w")
        authfile=open("authenticator.txt","w")
        l=[]
        authl=[]
        
        Name=input("Enter user name : ")
        l.append(Name)
        p=0
        while p<3:
            phnumber=input("Enter phone number : ")
            if len(phnumber)==10:
                l.append(phnumber)
                break
            else:
                print("Phone number must be of 10 digits!!!")
                p=p+1
        c=0
        while(c<3):
            email=input("Enter ur email : ")
            if email.endswith("@gmail.com"): 
                if email=='@gmail.com':
                    print("Try again")
                    c=c+1
                else:
                    l.append(email)
                    break
            else:
                print("Try agan")
                c=c+1
            
        AccNo = list(range(1000,9999))
        
        pd=0
        while pd<3:
            password=getpass.getpass("Enter pass: ")
            if len(password)>4 and len(password)<16:
                l.append(password)
                break
            else:
                print("Password must be in the length of between 4 and 16 characters")
                pd=pd+1
        
        l.append(password)
        authl.append(password)
        random.shuffle(AccNo)
        a=AccNo.pop()
        a2=a
        print("AccNo is : ",a)
        dataBase[a]=l
        authenticator[a2]=authl
        file.write(str(dataBase))
        authfile.write(str(authenticator))
        file.close()
        
        
def login():
    file=open("dataBase.txt","a+")
    if(os.path.getsize("dataBase.txt")==0):
        print("dataBase is empty Register and do login!!")
    else:
        c=0
        while c<3:
            a1=int(input("Enter ur account no. :"))
            p1=input("Enter ur password : ")
            authl=[]
            authfile=open("authenticator.txt","r")
            file=open("dataBase.txt","r")
            a=eval(file.read())
            a2=eval(authfile.read())
            if a1 in a2 and p1 in a2[a1]:
                print("Login sucessfully")
                a={"Balance":0,"Withdraw":[],"Deposit":[],"History":[]}
                dataBase[a1].append(a)
                main_Menu(a1)
                break
            else:
                print("wrong crentials!!! ")
                file.close()
                c=c+1
choice1=int(input("""Enter ur choice 
1--->Register Account
2--->login Account
3--->Quit"""))
while (choice1):
    if choice1==1:
        register()
        choice1=int(input("""Enter ur choice 
1--->Register Account
2--->login Account
3--->Quit"""))
    elif choice1==2:
        login()
        choice1=int(input("""Enter ur choice 
1--->Register Account
2--->login Account
3--->Quit"""))
    elif choice1==3:
        print("Thank u for using devil banking see you soon")
        break
    elif choice1!=1 and choice1!=2 and choice1!=3:
        print("wrong input enter correctly")
        print("""1--->Register Account
2--->login Account
3--->Quit""")
        choice1=int(input("Enter ur choice"))
