"""
Assume s is a string of lower case characters. Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
# COPILOT

s = 'azcbobobegghakl'

longest = ''
current = ''

for i in range(len(s)):
    if i == 0 or s[i] >= s[i - 1]:
        current += s[i]
        if len(current) > len(longest):
            longest = current
    else:
        current = s[i]


# longest string in alphabetical order
longest = ''
current = ''


for i in range(len(s)):
    if i == 0 or s[i] >= s[i - 1]:



print("Longest substring in alphabetical order is:", longest)