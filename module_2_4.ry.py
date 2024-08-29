numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    print(i)

while i < 2:
    is_prime = True
    for i in range(2, (i ** 0.5) + 1):
        if i % i == 0:
            is_prime = False
            break
        is_prime = True
        if is_prime:
           not_primes.append()
        else:
            primes.append()
print(primes)
print(not_primes)
