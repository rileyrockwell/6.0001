import time

def powers(a,b):
    return a**b

for i in range(2, 11):
    print("2**" + str(i) + ":", powers(2,i))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
for i in range(2, 11):
    print(str(i) + "!: ", factorial(i))
