def print_empty_rect():
    width = int((input("digite a largura: ")))
    height = int((input("digite a altura: "))) - 2
    line_drawing = "#" * width
    line_with_spaces = "#" + (" " * (width - 2)) + "#"

    print(line_drawing)
    for count in range(height):
        print(line_with_spaces)

    print(line_drawing)


print_empty_rect()
