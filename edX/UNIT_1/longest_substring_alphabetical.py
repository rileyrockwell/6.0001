"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.
"""

import string

s = 'azcbobobegghakl'
s = 'abcbcd'

lowercase = string.ascii_lowercase

lowercase_mapping = {letter: numerical_value for numerical_value, letter in enumerate(lowercase)}

# now that we have a mapping of the letters to their numerical values, we can iterate through the string and check if the next letter is greater than the previous letter, from the original string 's'.

alphabetical_substring = ''

for char in s:

# for each character in the string, s, we are triyng to determine the longest substring in alphabetical order.

# (1). create a list of each alphabetical substring. find the longest substring from the list.
# (2). 
# (3). 











