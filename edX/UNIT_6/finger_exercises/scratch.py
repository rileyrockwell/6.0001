def linearSearch(L, x):
	for e in L:
		if e == x:
			return True
	return False

def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total