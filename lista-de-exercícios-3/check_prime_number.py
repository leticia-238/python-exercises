n = int(input("Digite um número inteiro:"))
i = int(n ** (1/2))
is_prime = True

while i > 1 and is_prime:
    if n % i == 0:
        is_prime = False
    i -= 1

print("primo") if is_prime else print("não primo")