def soma_hipotenusas(n):
    i = 0
    h = 0
    sum_of_hypotenuses = set()

    while i < n:
        i += 1
        j = 1
        while j < n and j <= i:
            h = (i * i + j * j) ** (1 / 2)
            if h % int(h) == 0 and h <= n:
                print(i, j, h)
                sum_of_hypotenuses.add(h)
            j += 1

    return sum(sum_of_hypotenuses)
