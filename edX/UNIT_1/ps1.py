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
s = 'zyx'

lowercase = string.ascii_lowercase
lowercase_mapping = {letter: numerical_value for numerical_value, letter in enumerate(lowercase)}

for index in range(1, len(s)):
    numerical_value_initial = lowercase_mapping[s[index - 1]]
    numerical_value_subsequent = lowercase_mapping[s[index]]

    # if the letters are in alphabetical order
    if numerical_value_initial < numerical_value_subsequent:
        # keep track of multiple substrings simultaenously (if the need arises)
        
    
    
    # check to determine if 

    print(numerical_value_initial)
    print(numerical_value_subsequent)

