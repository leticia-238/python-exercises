n = input("Digite um número inteiro:")
quantity_of_digits = len(n)
number = int(n)
sum = 0

while quantity_of_digits > 0:
    power_of_ten = 10 ** (quantity_of_digits - 1)
    sum += number // power_of_ten
    number %= power_of_ten
    quantity_of_digits -= 1

print(sum)
