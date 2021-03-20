# Quiz Trivia Game
# File implementation for high scores categories question and answers
import os
import random


scoresheet = {}

def menu(): # function for menu

	print("	 	  ____            _            ____                    				")        
	print("		 /  _  \  _   _  (_)  ____    / ___|   __ _   _ __ ___     ___      ")
	print("		 | | | | | | | | | | |_  /   | |  _   / _` | | '_ ` _ \   / _ \		")
	print("		 | |_| | | |_| | | |  / /    | |_| | | (_| | | | | | | | |  __/		")
	print("		  \__\_\  \__,_| |_| /___|    \____|  \__,_| |_| |_| |_|  \___|		")
	print("		================================================================    ") 
	print()
	print("[1] Start Game")
	print("[2] About")
	print("[3] Highscores")
	print("[4] Exit")
	print()
	operator()

def operator(): # function for choosing an operaiton in the main menu
	operand = input("Please Choose an Operation: ")
	if operand == "1":
		start()
	elif operand == "2":
		about()
	elif operand == "3":
		dispscore()
	elif operand == "4":
		exit()
	else:
		print("Invalid Input, Please Choose again.")
		os.system("cls")
		menu()
		

def start(): #sub menu for choosing the quiz category
	os.system("cls")
	print("Please Select a category:")
	print()
	print("[1] Computers (no computation needed) - Easy")
	print("[2] Memes (mims not meh-mehs) - Medium")
	print("[3] Bleach (not used in laundry) - Hard")
	print("[4] Game of Thrones (not really a game) - Very Hard")
	print("[5] Back to Menu")
	print()
	category()


def category(): # sub operator for category
	category = input("Please choose a Category: ")

	if category == "1":
		comptree()
		
	elif category == "2":
		memetree()
		
	elif category == "3":
		bleachtree()
		
	elif category == "4":
		thronestree()
		
	elif category == "5":
		menu()

	else:
		print("Invalid Input, Please try again")
		start()

	
def about(): # Displays the about page, the instructions, and the details of the Quiz Categories.
	os.system("cls")
	print("This Game was made for a Project by Robie A. Carlos")
	print()
	print("Instructions: ")
	print("To start the game,type in the number 1 in the main menu then choose a category of your liking.")
	print("There are 4 Categories to choose from, each consists of 12 questions and randomly drawn from a question pool.")
	print()
	print("To sumbit your answer, simply type in the number beside your answer, there are 4 choices for each question,")
	print("so you will need to type in a number from 1-4, incorrect inputs such as other numbers or other characters will")
	print("result in a wrong answer.To quit mid-game, simply type in 'quitterako' and you'll be redirected to the main menu.")
	print(" ")
	print("If you score half or more than half of the total amount of points in a given category you will be")
	print("able to qualify for a highscore record and your name will be taken to be recorded as well.")
	print("To view all the highscores, simply type in the number 3 in the main menu and it will display all the highscores.")
	print("--------------------------------------------------------------------- ")
	print("The Computer Category is the easiest and requires basic knowledge of computers.")
	print("Each question in this category is worth 1 point.")
	print(" ")
	print("The Meme category has Medium difficulty and requires an intermediate understanding of memes")
	print("as well as their origins and where they are derived from.")
	print("Each question in this category is worth 2 points.")
	print(" ")
	print("The Bleach Category is placed in Hard difficulty and its questions are focused on Cloth Cleaning")
	print("products as well as some questions about detergents and fabric conditioners.")
	print("Each question in this category is worth 3 points.")
	print(" ")
	print("The Game of Thrones category is the most difficult question set in the quiz game.")
	print("The questions range from the names of places,characters, and specific objects in the TV series")
	print("Each question in this category amounts to 4 points.")
	print("---------------------------------------------------------------------- ")
	print("For suggestions and inquiries you may email me at racarlos1@up.edu.ph")
	print()

	menu()	


def dispscore(): # Displays The Highscores By name,category and score
	os.system("cls")
	print("          .-=========-.    ")
	print("          \*-=======-*/    ")
	print("          _|  ..=..  |_    ")
	print("         ((|  {{O}}  |))   ")
	print("          \|   /|\   |/    ")
	print("           \__ '`' __/     ")
	print("             _`) (`__      ")
	print("           _/_______\_     ")
	print("          /___________\    ")
	print( )

	print("These are the Highscores.")
	print()

	filescore = open("highscores.txt","r")
	highscores = []
	

	for line in filescore:
		score = line.split("-")
		highscores.append(score)

	n=0

	for x in highscores:	# gets the details of the highscore and diplays them per line 
		print("Name: ",highscores[n][0])
		print("Score: ",highscores[n][1])
		print("Category: ",highscores[n][2])
		n = n+1

	filescore.close()
	print()
	menu()


def exit(): #exit function
	print("Have a good day.")
	quit()


#----------------------------------------------------------------------------------------------------------------------
# Question Trees

def comptree(): # Computer Quiz Function
	os.system("cls")

	print("	                                                           ") #art hart
	print("		 _________        .-------------------.                ")  
	print("		:______.-':      :  .--------------.  :                ")  
	print("		| ______  |      | :                : |                ")
	print("		|:______B:|      | | COMPUTER QUIZ: | |                ")
	print("		|:______B:|      | |                | |                ")
	print("		|:______B:|      | |  Best of LUCK  | |                ")
	print("		|         |      | |    to you.     | |                ")
	print("		|:_____:  |      | |                | |                ")
	print("		|    ==   |      | :                : |                ")
	print("		|       O |      :  '--------------'  :                ")
	print("		|       o |      :'---...______...---'                 ")
	print("		|       o |-._.-i___|'             |._                 ")
	print("		|'-.____o_|   '-.   '-...______...-'  `-._             ")
	print("		:_________:      `.____________________   `-.___.-.    ")
	print("		                 .'.eeeeeeeeeeeeeeeeee.'.      :___:   ")
	print("		               .'.eeeeeeeeeeeeeeeeeeeeee.'.            ")
	print("		              :____________________________:           ")
	print("")
	print("")	
	print("Hello, you have chosen the Computer Category, this category revolves around basic")
	print("knowledge regarding computers.")
	print("Note: Remember to type in your answers correctly and be wary of the spaces.")
	print()	
	score = 0 

	filequestion = open("compquest.txt","r") # open the question text file 
	
	questionsheet = [] # this will store the questions line by line

	for line in filequestion: # gets the question from text file and transfers it to the questionsheet list
		randquest = line.split("-")
		questionsheet.append(randquest)
		
	filequestion.close() # if you open something then make sure to close it 
	
	count = 0
	while count<12:
		var = random.choice(questionsheet) #Picks a random question from the text file and displays it along with the choices
		print()
		print("[",count+1, "]",var[0])
		print("<>======================================================<>")
		print("(1)",var[1])
		print("(2)",var[2])
		print("(3)",var[3])
		print("(4)",var[4])
		print()

		answer = input("Enter your answer: ").lower() # takes the input for answer
		print()
		count = count+1
		questionsheet.remove(var) # removes entry to make way for next quest and set of choices

		if answer == var[5]: #in the answer if equal to the 5th detail then it is correct, otherwise wrong 
			score = score + 1
			print("The answer is correct.")
			print()

		elif answer == "quitterako":
			menu()

			print()
		else:
			print("The answer is incorrect.")
			print()

	print()
	print("Your score is: ",score,)
	print()


	if score >= 6: #if the score is equal to or greater than half their scores are qualified to be recorded

		print("Congratulations you have passed the quiz in Easy difficulty")
		print("Have you ever considered?, being a computer shop attendant?")
		print()
		name = input("Please Enter Your Name: ") #gets the name of the  player to be used as ID for score
		print(name,"your score will be put in the highscore records.")

		scoresheet = open("highscores.txt","a") #opens the highscore file and records the details
		scoresheet.write(name + "-" + str(score) +  "-" + "Computer" + "\n")
		scoresheet.close()


	else: 
		print("Sorry but you have failed the quiz, thus you will not be ")
		print("to qualify for the highscores.")
		print(" (ಠ_ಠ) ")

	print()
	print()
	print("You will now be redirected to the Main Menu.") # after the game ends the player will be redirected to the main menu
	print("Thank you for playing the Game.") # where they can view their highscore
	menu()

#----------------------------------------------------------------------------------------------------------------------


def memetree():
	os.system("cls")



	print("		░░░░░░░░░░░░░▄▄▄▄▄▄░░░░░░░░░░░░		")
	print("		░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░░░		")
	print("		░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░░░		")
	print("		░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░░░		")
	print("		░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░░░		")
	print("		░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░░░		")
	print("		░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░░░		")
	print("		░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░░░		")
	print("		░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░░░		")
	print("		░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░░░		")		
	print("		░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░░░		")
	print("		░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░░░		")
	print("		░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░░░		")
	print("		░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░░░		")
	print("		░░░░█░░░░░░░░░░░░░░░░░░░░░█░░░░		")
	print("		░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░░░		")
	print("		░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░░░		")
	print("")
	print("Hello, you have chosen the Meme Category, this category is focused on intermediate knowledge")
	print("of memes and their origins. Skrrrrrrrr!")
	print()
	print("Note: Remember to type in the number of your answer correctly.")
	print()
	score = 0 

	filequestion = open("memequest.txt","r")
	
	questionsheet = []

	for line in filequestion:
		randquest = line.split("-")
		questionsheet.append(randquest)
		
	filequestion.close()
	
	count = 0
	while count<12:
		var = random.choice(questionsheet)
		print("[",count+1, "]",var[0])
		print("<>======================================================<>")
		print("(1)",var[1])
		print("(2)",var[2])
		print("(3)",var[3])
		print("(4)",var[4])
		print()

		answer = input("Enter your answer: ").lower()
		print()
		count = count+1
		questionsheet.remove(var)

		if answer == var[5]:
			score = score + 2
			print("That's right!.")
			print()

		elif answer == "quitterako":
			menu()

		else:
			print("The answer is obviously wrong.")
			print()

	print()
	print("Your score is: ",score,)
	print()

	if score >= 12:
		print(" 												")
		print(" 	░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░	")
		print(" 	░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▀▄▄█▄░░░░▄░░░░█░░░░░░░	")
		print(" 	░░░░░░█▀░░░░░░░░░░░░░▀▀█▄░░░▀░░░░░░░░░▄░	")
		print(" 	░░░░▄▀░░░░░░░░░░░░░░░░░▀██░░░▄▀▀▀▄▄░░▀░░	")
		print(" 	░░▄█▀▄█▀▀▀▀▄░░░░░░▄▀▀█▄░▀█▄░░█▄░░░▀█░░░░	")
		print(" 	░▄█░▄▀░░▄▄▄░█░░░▄▀▄█▄░▀█░░█▄░░▀█░░░░█░░░	")
		print(" 	▄█░░█░░░▀▀▀░█░░▄█░▀▀▀░░█░░░█▄░░█░░░░█░░░	")
		print(" 	██░░░▀▄░░░▄█▀░░░▀▄▄▄▄▄█▀░░░▀█░░█▄░░░█░░░	")
		print(" 	██░░░░░▀▀▀░░░░░░░░░░░░░░░░░░█░▄█░░░░█░░░	")
		print(" 	██░░░░░░░░░░░░░░░░░░░░░█░░░░██▀░░░░█▄░░░	")
		print(" 	██░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░░░░▀▀█▄	")
		print(" 	██░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░▄▄██	")
		print(" 	░██░░░░░░░░░░░░░░░░░░▄▀░░░░░█░░░░░░░▀▀█▄	")
		print(" 	░▀█░░░░░░█░░░░░░░░░▄█▀░░░░░░█░░░░░░░▄▄██	")
		print(" 	░▄██▄░░░░░▀▀▀▄▄▄▄▀▀░░░░░░░░░█░░░░░░░▀▀█▄	")
		print(" 	░░▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░█▄▄▄▄▄▄▄▄▄██	")
		print(" 	░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░	")
		print("Congratulations you have passed the quiz in Medium difficulty")
		print("Have you considered being a meme?")
		print()
		name = input("Please Enter Your Name: ")
		print(name,"your score will be put in the highscore records.")

		scoresheet = open("highscores.txt","a")
		scoresheet.write(name + "-" + str(score) +  "-" + "Memes" + "\n")
		scoresheet.close()

	else: 
		print("Sorry but you have failed the quiz, thus you will not be ")
		print("to qualify for the highscores. Please educate yourself.")
		print("                          					") #ascii art
		print("		░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░			")
		print("		░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░			")
		print("		░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░			")
		print("		░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█░░░			")
		print("		░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█░░			")
		print("		█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█░			")
		print("		█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█			")
		print("		░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░			")
		print("		░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░			")
		print("		░░░█░░██░░▀█▄▄▄█▄▄█▄████░█░░░░			")
		print("		░░░░█░░░▀▀▄░█░░░█░███████░█░░░			")
		print("		░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░			")
		print("		░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█░░░░ 			")
		print("		░░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▄▄░█░░░░ 			")

	print()
	print("You will now be redirected to the Main Menu.")
	print("Thank you for playing the Game.")
	menu()

#----------------------------------------------------------------------------------------------------------------------

def bleachtree():
	os.system("cls")
	print("Hello, you have chosen the Bleach Category, this category is about the Anime Bleach by Tite Kubo.")
	print("The questions here revolves throughout the whole series,being very specific in detail.")
	print("Note: Remember to type in your answers correctly and be wary of the spaces.")
	print()
	score = 0 

	filequestion = open("bleachquest.txt","r")
	
	questionsheet = []

	for line in filequestion:
		randquest = line.split("-")
		questionsheet.append(randquest)
		
	filequestion.close()
	
	count = 0
	while count<12:
		var = random.choice(questionsheet)
		print()
		print("[",count+1, "]",var[0])
		print("<>======================================================<>")
		print("(1)",var[1])
		print("(2)",var[2])
		print("(3)",var[3])
		print("(4)",var[4])
		print()

		answer = input("Enter your answer: ").lower()
		print()
		count = count+1
		questionsheet.remove(var)

		if answer == var[5]:
			score = score + 3
			print("The answer is correct.")
			print()

		elif answer == "quitterako":
			menu()

		else:
			print("The answer is incorrect.")
			print()

	print()
	print("Your score is: ",score,)
	print()



	if score >= 18:

		print("	._._._._._._._._._|_____________________________________________________________________	")
		print("	|_|_|_|_|_|_|_|_|_|____________________________________________________________________/ 	")
		print()              
		print("Congratulations you have passed the quiz in Hard difficulty")
		print("The Soul King smiles upon you.")
		print()
		name = input("Please Enter Your Name: ")
		print(name,"your score will be put in the highscore records.")

		scoresheet = open("highscores.txt","a")
		scoresheet.write(name + "-" + str(score) +  "-" + "Bleach" + "\n")
		scoresheet.close()

	else: 
		print("Sorry but you have failed the quiz, thus you will not be able ")
		print("to qualify for the highscores. ")
		print("Such a shame.")

	print()
	print("You will now be redirected to the Main Menu.")
	print("Thank you for playing the Game.")
	menu()

#----------------------------------------------------------------------------------------------------------------------

def thronestree():
	os.system("cls")		
	print()	                          		    
	print("	                   		   ( ((   		            ")
	print("		                           ) ))				")
	print("		  .::.                    / /(				")
	print("		 'O .-;-.-.-.-.-.-.-.-.-/| ((:::::::::::::::::::::::::::::::::::::::::::::::::::::::::._    ")
	print("		(O ( ( ( ( ( ( ( ( ( ( ( |  ))   =================================================-    _.>  ")
	print("		 `O `-;-`-`-`-`-`-`-`-`-\| ((:::::::::::::::::::::::::::::::::::::::::::::::::::::::::''    ")
	print("		  `::'                    ) \(            ")
	print("		                           ) ))            ")
	print("		                          (_((             ")
	print()
	print()
	print("Hello, you have chosen the Game of Thrones Category, the questions here are about the ever changing world of Westeros.")
	print("Character, places, and objects of interest are the particular topic of this quiz.")
	print("Note: Remember to type in the number of your answer correctly.")
	print()
	score = 0 

	filequestion = open("thronequest.txt","r")
	
	questionsheet = []

	for line in filequestion:
		randquest = line.split("-")
		questionsheet.append(randquest)
		
	filequestion.close()
	
	count = 0
	while count<12:
		var = random.choice(questionsheet)
		print()
		print("[",count+1, "]",var[0])
		print("<>======================================================<>")
		print("(1)",var[1])
		print("(2)",var[2])
		print("(3)",var[3])
		print("(4)",var[4])
		print()

		answer = input("Enter your answer: ").lower()
		print()
		count = count+1
		questionsheet.remove(var)

		if answer == var[5]:
			score = score + 4
			print("The answer is correct.")
			print()

		elif answer == "quitterako":
			menu()

		else:
			print("The answer is incorrect.")
			print()

	print()
	print("Your score is: ",score,)
	print()


	if score >= 24:
		print()
		print("	   |\                     /) 	")
		print("	 /\_\\__               (_// 	")
		print("	|   `>\-`     _._       //`)	")
		print("	 \ /` \\  _.-`:::`-._  // 		")
		print("	  `    \|`    :::    `|/ 		")
		print("	        |     :::     | 		")
		print("	        |.....:::.....| 		")
		print("	        |:::::::::::::|			")
		print("	        |     :::     |			")
		print("	        \     :::     /			")
		print("	         \    :::    /			")
		print("	          `-. ::: .-'			")
		print("	           //`:::`\\			")
		print("	          //   '   \\			")
		print("	         |/         \| 			")
		print()
		print("Congratulations you have passed the quiz in BERI  Hard difficulty")
		print("The long night has come, but Season 8 still hasn't.")
		print()
		name = input("Please Enter Your Glorious Name: ")
		print(name,"your score will be put in the highscore records.")

		scoresheet = open("highscores.txt","a")
		scoresheet.write(name + "-" + str(score) +  "-" + "GOT" + "\n")
		scoresheet.close()


	else: 
		print("Sorry but you have failed the quiz, thus you will not be ")
		print("to qualify for the highscores. ")
		print("		               ______                           ")
		print('	                    .-"      "-.  					')
		print("	                   /            \					")
		print("	       _          |              |          _      	")
		print("	      ( \         |,  .-.  .-.  ,|         / )		")
		print("	       > '=._     | )(__/  \__)( |     _.=' <		")
		print('	      (_/"=._"=._ |/     /\     \| _.="_.="\_)      ')
		print("	             '=._ (_     ^^     _)'_.='				")
		print("	                 '=\__|IIIIII|__/='					")
		print("	                _.='| \IIIIII/ |'=.					")
		print('	      _     _.="_.="\          /"=._"=._     _      ')
		print('	     ( \_.="_.="     `--------`     "=._"=._/ )		')
		print('	      > _.="                            "=._ <		')
		print('	     (_/                                    \_)		')

	print()
	print("You will now be redirected to the Main Menu.")
	print("Thank you for playing the Game.")
	menu()


#----------------------------------------------------------------------------------------------------------------------	
#Start of Execution


menu()

