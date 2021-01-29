from chatbot.activities import *
import datetime

name=input("What shall I call you, my friend?: ").capitalize()
name_list=[]
name_list.append(name)
date=[]
time=[]
task=[]
def entertain():
    print("Hey, ",name,"! Nice to see you.",sep="")
    print("I am here to help you.")
    while True:
        choice=input("What do you want me to do?:")
        task.append(choice)
        t_date=datetime.date.today()
        date.append(str(t_date))
        t_time=datetime.datetime.now().time()
        time.append(str(t_time))

        if choice.lower()=="history" or choice.lower()=="see history" or choice.lower()=="delete history" or choice.lower()=="filter history":
            pass
        else:
            fn="history.csv"
            f=open(fn,'a', newline='')
            s_writer=csv.writer(f)
            #s_writer.writerow(["Name","Date","Time","Task"])
            n=name_list[-1]
            d=date[-1]
            t=time[-1]
            ta=task[-1]
            lst=[n,d,t,ta]
            s_writer.writerow(lst)
            f.close()

        if choice.lower()=="joke":
            print("Sad? I will refresh your mood :D")
            joke()

        elif choice.lower()=="riddle" or choice.lower()=="riddles":
            riddles()

        elif choice.lower()=="play a game" or choice.lower()=="game" or choice.lower()=="play":
            print("""
            Which game?
            a) Rock, Paper, Scissors
            b) Hangman  (*NEW*)
            MORE TO COME...
            """)
            choose=input("Enter choice(a/b): ")
            if choose=='a':
                stone_paper_scissors()
            elif choose=='b':
                hangman()
            else:
                print("Wrong Choice.")

        elif choice.lower()=="stopwatch" or choice.lower()=="watch" or choice.lower()=="time":
            stopwatch()

        elif choice.lower()=="to do list" or choice.lower()=="task list" or choice.lower()=="task" or choice.lower()=="to do":
            todo()

        elif choice.lower()=="open youtube" or choice.lower()=="web browser" or choice.lower()=="search" or choice.lower()=="open facebook":
            search()

        elif choice.lower()=="see history" or choice.lower()=="history":
            f=open("history.csv",'r')
            s_reader=csv.reader(f)
            for rec in s_reader:
                print(rec[0],rec[1],rec[2],rec[3],sep="\t\t\t")

        elif choice.lower()=="filter history":
            f=open("history.csv",'r')
            inp=input("Enter name: ")
            s_reader=csv.reader(f)
            for rec in s_reader:
                if rec[0]==inp.capitalize():
                    print(rec[0],rec[1],rec[2],rec[3],sep="\t\t\t")

        elif choice.lower()=="delete history":
            inp=input("Enter name: ")
            with open ("history.csv") as f:
                updated=[]
                found=0
                reader_obj=csv.reader(f)
                for rec in reader_obj:
                    if rec[0]==inp:
                        found=1
                    else:
                        updated.append(rec)
            if found==0:
                print("no record found")
            else:
                with open('history.csv','w') as f:
                    writer_obj=csv.writer(f,lineterminator='\n')
                    writer_obj.writerows(updated)

        else:
            print("Sorry, I can't understand. May be I need to go to school again.")
            print("""TRY:
            # Joke
            # Riddle
            # Play a game
            # To Do list
            # Stopwatch
            # Open Youtube/Twitter/Instagram/Facebook/Gmail or Search anything
            # See history
            # Filter history
            # Delete history
            """)

        cont=input("need more help? (y/n) ")
        if cont.lower()=="n":
            print("Always there for you :) \n Byee")
            break

entertain()
