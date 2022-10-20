n = int(input("Digite o valor de n:"))
i = 0

while n > 0:
    if i % 2 != 0:
        print(i)
        n -= 1
    i += 1