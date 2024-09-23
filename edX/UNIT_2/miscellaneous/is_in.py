def isIn(char, aStr):
	"""
	determines if char is in aStr using bisection search, recursively

	char: a single character aStr: an alphabetized string (i.e. a
	string w/ characters in alphabetical order)

	returns: True is char is in aStr; False otherwise
	"""
	if len(aStr) == 0:
		return False

	# Find the middle index and middle character
	mid_index = len(aStr) // 2
	mid_char = aStr[mid_index]

	# Base case: If the middle character is the target, return True
	if char == mid_char:
		return True

	# Recursive case: if char is smaller than mid_char
	elif char < mid_char:
		# set the upper bound and run again
		return isIn(char, aStr[:mid_index])

	# Recursive case: if char is larger than mid_char
	else:
		# set the lower bound and run again
		return isIn(char, aStr[mid_index + 1:])


print(isIn('d', 'abcdefg'))