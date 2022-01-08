# Friendaid-chatbot
FriendAid- the chatbot is a user-friendly menu driven program that is made to allow user to perform multiple functions for entertainment. It also gives the option to search through the web and to land to some popular sites like Facebook and Twitter, making social media available at one click.
The focus of this project as the name itself suggests is to be the user’s friend through various options of entertainment like games, riddles and by allowing the user to keep a track on himself through stopwatch and to-do- list. The user can also browse through his previous history. 

The project is made using Python, Python-CSV connectivity and Tkinter and other modules of Python.

FEATURES:
1) History
    See history
    Filter History
    Delete History
    
2) Web Functions
    Open YouTube
    Open social networking sites
    Search on web
    
3) Entertainment
    Riddles
    Games
    Jokes
    
4) Stopwatch

5) To Do list

<h3>Python Modules And In-Built Functions</h3>
random
	 Python offers random module that can generate random numbers
random.choice(<list>): It is used to select a random element from the list

time
	This module provides various time-related functions.
time.time(): The time() function returns the number of seconds passed since epoch (the point where time begins)

webbrowser
	The webbrowser module includes functions to open URLs in interactive browser applications. 
webbrowser.open_new(): This opens the requested page using the default browser.

csv
	csv module is used to establish python- csv connectivity. The csv module implements classes to read and write tabular data in CSV format.
  
tkinter
	Tkinter is the standard GUI library for  Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.
tkinter.Label(): A label is a text used to display some message or information about the other widgets.
tkinter.Button(): The Button is used to add various kinds of buttons to the python application.

datetime
	The datetime module supplies classes for manipulating dates and times.
datetime.date.today():displays the current date
Datetime.datetime.now().time: displays the current time

<h3>Project Glossary</h3>
The project consists of 2 files:
activities.py
func_call.py

activities.py contains all the activities that can be performed by FRIENDAID. The functions contained are:

	joke(): This functions opens the window that displays jokes.

	riddles(): This functions opens the window that displays riddles.

	stone_paper_scissors(): This function allows the user to play rock paper scissors game with the bot.

	hangman(): The  function allows the user to play hangman game.
  
  	todo(): This function offers to do list to the user in which he can store his tasks and delete them after completing.

	search(): This function opens the web browser for the user which allows him to open Facebook, YouTube, Instagram, twitter, Gmail and also allows user to search anything over web.

 	stopwatch(): This function makes the stopwatch accessible to the user.

func_call.py contains the function entertain() which helps the user to interact with the chatbot and makes all the functions accessible to the user (that are defined in activities.py).
