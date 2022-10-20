s = input("Digite um número inteiro:")
index = 0
has_adjacent_equal = False

while index < len(s) - 1 and not has_adjacent_equal:
  if int(s[index]) == int(s[index + 1]):
    has_adjacent_equal = True
  index += 1
  
print("sim") if has_adjacent_equal else print("não")