"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
count = 0
n = len('bob')

for i in range(len(s)- n):
    if s[i: i + n] == 'bob':
         count += 1

print('Number of times bob occurs is: ', count)