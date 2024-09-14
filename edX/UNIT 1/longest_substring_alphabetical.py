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

lowercase = string.ascii_lowercase

index_dictionary = {letter: index for index, letter in enumerate(lowercase)}

substring = ""
results = []

s = 'azcbobobegghakl'
s = 'abcbcd'


for index in range(1, len(s)):
    a = s[index - 1]
    b = s[index]

    if index_dictionary[a] <= index_dictionary[b]:
        substring += a
        length = len(substring)
    else:
        # do not like the following line
        substring += a
        results.append(substring)
        substring = ""

# print the longest length in results (consolidates based on numerical value of key)
results_dict = {len(string): string for string in results}
max_length_string = int(max(results_dict.keys()))
print(results_dict[max_length_string])