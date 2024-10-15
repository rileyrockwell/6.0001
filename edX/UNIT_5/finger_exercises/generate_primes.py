def genPrimes():
    prime_list = []
    candidate = 2
    while True:
        is_prime = True
        for prime in prime_list:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(candidate)
            yield candidate
        candidate += 1

print(genPrimes())