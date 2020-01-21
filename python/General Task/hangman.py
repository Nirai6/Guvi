import random
words=["cat","dog","india","ant","rain"]
word=random.choice(words)
print("\nWelcome to Hangman")
q=input("\npress any key to continue: ")
i=0
c=''
guesses=''
length=len(word)
while(i<10):
    attempt=0
    for c in word:
        if c in guesses:
            print(c,end="  ")
        else:
            print(end=" _ ")
            attempt=attempt+1
    if attempt==0:
        print("\n\n ******You won****** ")
        print("\n",word,"is correct guess")
        break
    guess=input("\n\n Guess the letter : ")
    guesses=guess+guesses
    
    if guess not in word:
        print("Wrong you have : ",9-i," attempts")
        i=i+1
        if i==10:
            print("Game over")
        
    

