from math import factorial


n = int(input("Digite o valor de n:"))
factorial = 1

while n > 0:
  factorial *= n
  n -= 1

print(factorial)