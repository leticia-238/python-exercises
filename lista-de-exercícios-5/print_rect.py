def print_rect():
    width = int((input("digite a largura: ")))
    height = int((input("digite a altura: ")))
    count = 1
    line_drawing = "#" * width

    while count <= height:
        print(line_drawing)
        count += 1


print_rect()
