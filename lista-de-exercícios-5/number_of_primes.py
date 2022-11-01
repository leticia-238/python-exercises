def is_prime(n):
    i = int(n ** (1 / 2))
    is_prime = True

    while i >= 2 and is_prime:
        if n % i == 0:
            is_prime = False
        i -= 1
    return is_prime


def n_primos(n):
    primes = 0
    current_number = 2
    while current_number <= n:
        if is_prime(current_number):
            primes += 1
        current_number += 1
    return primes
