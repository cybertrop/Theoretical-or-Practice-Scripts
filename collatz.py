#!/bin/python

# Collatz Sequencing Script 
def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number // 2
	elif number % 2 == 1:
		result = 3 * number + 1
		print(result)
		return result
try:
	n = input("Enter an integer please: ")
	while n != 1: # We are going to loop while n is not equal to one until we reach one ; hence the Collatz sequence
		n = collatz(int(n))
		
except ValueError:
	print("Please type an integer! ")


collatz(12)
