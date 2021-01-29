import random
import time
import webbrowser
import csv
from tkinter import *
def joke():
    def display():
        jokes=[1,2,3,4,5,6,7,8]
        a=random.choice(jokes)
        if a==1:
            l1.configure(text="Student: will you punish me for what i have not done \nTeacher: No! \nStudent: I have not done my homework")
        elif a==2:
            l1.configure(text="Knock on door: \nMan: Who's this? \nPolice: Police \nMan: What do you want?(Does not open door) \nPolice: Talk to you \nMan: how many of you are there? \nPolice:2 \nMan:Then talk to each other")
        elif a==3:
            l1.configure(text="Manager: What is your qualification? \nPappu: I’m Ph.D. \nManager: What do you mean by Ph.D.? \nPappu: Passed high school with difficulty.")
        elif a==4:
            l1.configure(text="Wife: whenever we keep the money in the bags our son steals it,\n I don’t know what to do? \nHusband: Keep it in his books. I know he will never touch them!")
        elif a==5:
            l1.configure(text="Why was the birthday cake as hard as a rock? \n Because it was marble cake!")
        elif a==6:
            l1.configure(text="Barista: How do you take your coffee? \n Me: Very, very seriously.")
        elif a==7:
            l1.configure(text="What do you call friends who love math? \n A: algebros")
        else:
            l1.configure(text="How to reduce weight? \nFirst turn your head to the right and then to the left. \n\n\nRepeat this one whenever you have given something to eat!")

    def clear():
        l1.configure(text=" ")

    root=Tk()
    root.title("JOKES")
    root.geometry("500x300")
    root.configure(bg="#7B7B7B")

    l1=Label(root,text=" ",font=12,fg="#440359")
    l1.place(x=5,y=5, height=200, width=490)
    b1=Button(root,text="JOKE",bg='#CD5151',fg='#FFFFFF',command=display).place(x=20,y=220,height=50,width=60)
    b2=Button(root,text="CLEAR",bg='#CD5151',fg='#FFFFFF',command=clear).place(x=100,y=220,height=50,width=60)

    root.mainloop()


def riddles():
    def display():
        riddle=[1,2,3,4,5,6,7]
        global a
        a=random.choice(riddle)
        if a==1:
            l1.configure(text="Riddle: What can’t talk but will reply when spoken to? ")
        elif a==2:
            l1.configure(text="Riddle: The more of this there is, the less you see. What is it? ")
        elif a==3:
            l1.configure(text="Riddle: David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?")
        elif a==4:
            l1.configure(text="Riddle: What can you hold in your left hand but not in your right? ")
        elif a==5:
            l1.configure(text="Riddle: Why was the birthday cake as hard as a rock? ")
        elif a==6:
            l1.configure(text="Riddle: What has T in the beginning, T in the middle, and T at the end?  ")
        else:
            l1.configure(text="Riddle: Where does today come before yesterday? ")

    def clear():
        l1.configure(text=" ")
        l2.configure(text=" ")

    def check():
        if a==1:
            l2.configure(text="Answer: An echo")
        elif a==2:
            l2.configure(text="Answer: Darkness")
        elif a==3:
            l2.configure(text="Answer: David ")
        elif a==4:
            l2.configure(text="Answer: Your right elbow ")
        elif a==5:
            l2.configure(text="Answer: Because it was marble cake! ")
        elif a==6:
            l2.configure(text="Answer: A teapot. ")
        else:
            l2.configure(text="Answer: The dictionary ")


    root=Tk()
    root.title("RIDDLES")
    root.geometry("500x300")
    root.configure(bg="#6EC2F5")

    l1=Label(root,text=" ",fg='#440359')
    l2=Label(root,text=" ",fg='#440359')
    l1.place(x=5,y=2, height=50, width=490)
    l2.place(x=5,y=100, height=40, width=490)
    b1=Button(root,text="RIDDLE",bg='#CD5151',fg='#FFFFFF',command=display).place(x=20,y=200,height=50,width=60)
    b2=Button(root,text="CLEAR",bg='#CD5151',fg='#FFFFFF',command=clear).place(x=100,y=200,height=50,width=60)
    b2=Button(root,text="ANSWER",bg='#CD5151',fg='#FFFFFF',command=check).place(x=200,y=200,height=50,width=60)
    root.mainloop()

def stone_paper_scissors():
    while True:
        game=["Rock","Paper","Scissors"]
        a=random.choice(game)
        choose=input(" Rock,Paper or scissors?:").capitalize()
        time.sleep(2)
        print("Choice of computer: ",a)
        if a==choose:
            print("DRAW")
        elif a==game[0]:
            if choose=="Paper":
                print("Yah!, you win. You seem to be a good player")
            elif choose=="Scissors":
                print("Oh! you lose. Better luck next time")
        elif a==game[1]:
            if choose=="Rock":
                print("Oh! you lose. Better luck next time")
            elif choose=="Scissors":
                print("Yah!, you win. You seem to be a good player")
        elif a==game[2]:
            if choose=="Rock":
                print("Yah!, you win. You seem to be a good player")
            elif choose=="Paper":
                print("Oh! you lose. Better luck next time")
        cont=input("CONTINUE STONE PAPER SCISSORS?(y/n): ").upper()
        if cont=="N":
            break

def hangman():
    words=['CYCLE','BLACK','SHIRT','STRAWBERRY','DAFFODIL','BLAZER','CRYSANTHEMUM',"WALRUS","BLAZER","TURQUOISE","VIOLET","VIOLET","CHIMPANZEE","CHERRY"]
    hints=['transport',"colour",'clothes','fruit','flower','clothes','flower',"Animal","clothes","colour","flower","colour","animal","fruit"]
    choice=True
    while choice==True:
        guessed_letters=[]
        guessed=False
        life=8
        a=random.choice(words).upper()
        complete_word="_ "*len(a)
        print("Let's play Hangman!")
        print("hint: ",hints[words.index(a)])
        print('\n')
        print(complete_word)
        print('\n\n')
        list_word=complete_word.split()
        while (not guessed and life >0):
            guess=input("Guess the letter in this word: ").upper()
            if guess in guessed_letters:
                print("you have already guessed this letter. TRY AGAIN ")
            elif guess not in a:
                print("This letter is not in the word. Try again")
                life-=1
                guessed_letters.append(guess)
                print("tries left: ",life)
                print(list_word)
            elif guess in a:
                for i in range(len(a)):
                    if guess==a[i]:
                        list_word.pop(i)
                        list_word.insert(i,guess)
                print(list_word)
                guessed_letters.append(guess)
            if list_word==list(a):
                print("The letter guessed by you is CORRECT.\n You are a genius")
                guessed=True
            if life==0:
                print("Sorry, you are out of life. the correct word is: ",a)
        choose=input("Play HANGMAN again?(Y/N):" ).upper()
        if choose=="N":
            choice=False
        else:
            choice=True

def todo():
    task={}
    def append():
        n=int(input("Enter the number of tasks to be completed: "))
        for i in range(n):
            complete=input("Enter the task to be completed: ")
            task[(i+1)]=complete
    def show():
        for i in task:
            print(i,":",task[i])
    def delete():
        cont='y'
        while cont in 'Yy':
            number=int(input("Enter the task number of task completed: "))
            task.pop(number)
            cont=input("Delete more tasks?")
    menu="""TO DO LIST
    1) Add tasks
    2) Show the tasks to be completed
    3) Delete task
    0) Exit"""
    while True:
        print(menu)
        inp=int(input("What to do?: "))
        if inp==1:
            append()
            input()
        elif inp==2:
            show()
            input()
        elif inp==3:
            delete()
            input()
        elif inp==0:
            break
        else:
            print("UNIDENTIFIED REQUEST")
            input()

def search():
    root=Tk()
    root.title("WEB BROWSER")
    root.geometry("400x150")

    def fb():
        webbrowser.open_new("https://www.facebook.com/")
    def yt():
        webbrowser.open_new("https://www.youtube.com/")
    def ig():
        webbrowser.open_new("https://www.instagram.com/")
    def tw():
        webbrowser.open_new("https://www.twitter.com/")
    def gmail():
        webbrowser.open_new("https://www.gmail.com/")
    def search():
        word=(x.get()).split()
        s=""
        for i in word:
            s=s+i+"+"

        search='https://www.google.com/search?q='+s
        webbrowser.open_new(search)
    x=StringVar()
    b1=Button(root,text="Facebook",fg="#FFFFFF",bg="#0050E4",command=fb).place(x=10,y=70,width=80,height=30)
    b2=Button(root,text="Youtube",fg="#FFFFFF",bg="#FF0000",command=yt).place(x=100,y=70,width=80,height=30)
    b3=Button(root,text="Instagram",fg="#FFFFFF",bg="#EB007E",command=ig).place(x=190,y=70,width=80,height=30)
    b4=Button(root,text="Twitter",fg="#FFFFFF",bg="#0099DA",command=tw).place(x=10,y=105,width=135,height=30)
    b5=Button(root,text="Gmail",fg="#FFFFFF",bg="#591E1E",command=gmail).place(x=155,y=105,width=135,height=30)
    b6=Button(root,text="Search",fg="#FFFFFF",bg="#043202",command=search).place(x=320,y=10,width=70,height=50)
    e1=Entry(root,textvariable=x).place(x=10,y=10,width=300,height=50)
    root.mainloop()

def stopwatch():
    print("Press ENTER to start the watch")
    input()
    start=time.time()
    print("Stopwatch Started")
    print("Press ENTER to stop the watch")
    input()
    stop=time.time()
    t=stop-start
    hr=int(t//120)
    minute=int(t//60)
    sec=int(t%60)
    print("Stopwatch Stopped")
    print("Time taken: ")
    print(hr,"hr:",minute,"min:",sec,"sec",sep=" ")

if __name__=='__main__':
    riddles()
    stone_paper_scissors()
    hangman()
    stopwatch()
    todo()
    search()
    joke()
