#!/bin/python

# Collatz Sequencing Script 
# Currently in the works; almost done

import sys

def collatz(number):
	if number % 2 == 0:
		result = number // 2 
		print result
		return
	else:
		number % 2 == 1
		result2 = 3 * number + 1
		print result2
		return		

def user_choice():
	while True:
		print('Please choose type an integer')
		user_choice = int(input())
		print ('You choose ' + str(user_choice) + ' and the result for the first function is...') 
		result = collatz(user_choice)
		if result == 1:
			sys.exit(0)
		

user_choice()
print('Everything below is output from the first function..')
collatz(1)
collatz(2)
collatz(3)
collatz(4)
