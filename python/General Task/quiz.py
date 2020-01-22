q1='''Who is captain of indian cricket team?
a) virat kohli
b) ms dhoni
c) rohith sharma
d) sachin'''
q2='''Who  is the owner of tesla corp ?
a) steve jobs
b) elon musk
c) mark juckerberg
d) bill gates'''
q3='''Whic country won most world cups in odi ?
a) england
b) india
c) australia
d) westindies'''
q4='''Who is pawan sherawart?
a) cricket player
b) football player
c) hockey player
d) kabaddi player'''
count=0
pts=1
name=input("Enter ur name to continue: ")
print("Welcome ",name,)
print("""Rules are:
1)Correct answer = 5pts
2)Wrong answer= -2pts
3)Minimum 10 pts to sucessfully complete the quiz""")
a=input("press any key to continue")
questions={q1:"a",q2:"b",q3:"c",q4:"d"}
for i in questions:
    print(i)
    ans=(input("enter the answer: "))
    if ans==questions[i]:
        count=count+1
        pts=count*5
    else:
        count=count-1
        pts=pts-2
        
    
if pts>10:
        print("You have answered",count,"questions correctly")
        print("Your score is",pts)
        print("You have sucessfully completed the quiz")
    
else:
        print("You have failed to clear the quiz")
        

    
    
