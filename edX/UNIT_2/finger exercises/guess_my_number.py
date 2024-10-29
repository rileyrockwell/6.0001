def guess_my_numbers():
	"""
	The program works as follows: you (the user) thinks of an integer
	between 0(inclusive) and 100 (not inclusive). The computer
	makes guesses, and you give it input - is its guess too high
	or too low? Using bisection search, the computer will guess
	the user's secret number!

	- Your program should use bisection search. So think carefully
	what that means. What will the first guess always be? How
	should you calculate subsequent guesses?

	- Your initial endpoints should be 0 and 100. Do not optimize
	your subsequent endpoints by making them be the halfway point
	plus or minus 1. Rather, just make them be the halfway point.

	- Your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

	- When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input.
			
	return: str (correct / incorrect)

	"""
	response = ''
	low = 0
	high = 100
	guesses = 0

	print('Please think of a number 0 <= x < 100!')

	while response != 'c':
		# reset 'response' each time
		response = ''

		# initial bisection step
		guess = (low + high) // 2

		# user input response (ensure input is correct)		
		while response not in ['h', 'l', 'c']:
	
			# prompt user with guess each time
			print('Is your secret number:', str(guess) + '?')

			# obtain user input
			response = str(input(
				'Enter \'h\' to indicate the guess is too high. \n'
				'Enter \'l\' to indicate the guess is too low. \n' 
				'Enter \'c\' to indicate the computer is correct \n'
				'Response: '))

			# if valid user input
			if response in ['h', 'l', 'c']:
				# break out of the user input loop
				break

			# if invalid user input
			if response not in ['h', 'l', 'c']:
				print('Sorry, I do not understand your input. Please select \'h\', \'l\', or \'c\' .')
		


		# BISECTION METHOD
		if response == 'h':
			# discard the 'upper half' of the search space, 
			# by intializing the 'upper bound' of the search space 
			# such that all guesses afterward must be below this 
			# 'upper bound'
			# i.e. 50 (original guess) is the upper bound
			high = guess


		elif response == 'l':
			# discard the 'lower half' of the search space, 
			# by initializing the 'lower bound' of the search space
			# such that all guesses afterward must be above this
			# 'lower bound'
			# i.e. 50 (original guess) is the lower bound			
			low = guess

		# recompute guess (completed at the top of the loop)
		# guess = (low + high) // 2


	# indicate the game is over and display the results
	guess = (low + high) // 2
	return 'Good guess! Your secret number was: ' + str(guess) + '.'




# TO SUBMIT
# TO SUBMIT
response = ''
low = 0
high = 100
guesses = 0

print('Please think of a number between 0 and 100!')

while response != 'c':
	# reset response each time
	response = ''

	# initial bisection step
	guess = (low + high) // 2

	# ensure input is correct
	while response not in ['h', 'l', 'c']:

		# prompt user with guess each time
		print('Is your secret number', str(guess) + '?')

		# obtain user input
		response = str(input(
			'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. '))

		# if valid user input
		if response in ['h', 'l', 'c']:
			# break out of the user input loop
			break

		# if invalid user input
		if response not in ['h', 'l', 'c']:
			print('Sorry, I do not understand your input. Please select \'h\', \'l\', or \'c\' .')
	


	# BISECTION METHOD
	if response == 'h':
		# discard the 'upper half' of the search space, 
		# by intializing the 'upper bound' of the search space 
		# such that all guesses afterward must be below this 
		# 'upper bound'
		# i.e. 50 (original guess) is the upper bound
		high = guess


	elif response == 'l':
		# discard the 'lower half' of the search space, 
		# by initializing the 'lower bound' of the search space
		# such that all guesses afterward must be above this
		# 'lower bound'
		# i.e. 50 (original guess) is the lower bound			
		low = guess

	# recompute guess (completed at the top of the loop)
	# guess = (low + high) // 2


# indicate the game is over and display the results
guess = (low + high) // 2
print('Game over. Your secret number was:', guess)