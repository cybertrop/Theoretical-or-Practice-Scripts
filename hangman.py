#!/bin/python

# This is going ot be our hangman program! 

def hangman(word): # Create the hangman function to store this game; the func accepts the word as a parameter (the word for Player 2 to guess)
	wrong = 0 # This func sets a variable called wrong and sets its value to zero and keep track of wrong words
	
# Here we are going to create the stages as a list. There will be 8 stages total and with each stage an image of a picture appears. 
	stages = ["",
				" ___________           ",
				"|                      ",
				"|           |          ",
				"|           0          ",
				"|          /|\         ",
				"|          / \         ",
				"|                      ",
				]

	rletters = list(word) # this is a list containing each character in the variable word that keeps track of which letter are left to guess
	board = ["__"] * len(word) # This var is a list of strings used to keep track of the hints you display to Player 2. For example c__t if the word is cat
				#+ You use this statment to populate the board list with an underscore for every character in the variabler word.
	win = False # Keeps track if Player 2 has won the game 
	print("Welcome to Hangman! ")


	while wrong < len(stages) - 1:
		print("\n")
		msg = "Guess a letter "
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "__" not in board:
			print("You win! ")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0:wrong]))
		print("You lose! It was {}.".format(word))

hangman("cat")
