def get_numbers():
    numbers = []
    n = 1
    while n != 0:
        n = int(input("Digite um número: "))
        numbers.append(n)
    numbers.pop()
    return numbers


def print_inverted_numbers(numbers: list):
    index = len(numbers) - 1
    while index >= 0:
        print(numbers[index])
        index -= 1


def main():
    numbers = get_numbers()
    print_inverted_numbers(numbers)


main()
