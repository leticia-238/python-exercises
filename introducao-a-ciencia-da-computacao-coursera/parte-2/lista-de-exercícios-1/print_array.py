def imprime_matriz(matriz):
    for i, line in enumerate(matriz):
        line_str = []
        for elem in line:
            line_str.append(f"{elem}")
        print(" ".join(line_str))
