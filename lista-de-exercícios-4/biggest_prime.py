def check_prime_number(number):
    is_prime = True
    i = int(number ** (1 / 2))

    while i > 1 and is_prime:
        if number % i == 0:
            is_prime = False
        i -= 1
    return is_prime


def maior_primo(number):
    is_prime = check_prime_number(number)
    while not is_prime:
        number -= 1
        is_prime = check_prime_number(number)

    return number
