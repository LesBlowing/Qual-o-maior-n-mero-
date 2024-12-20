numero_1 = int(input("Digite o primeiro número:"))
numero_2 = int(input("Digite o segundo número:"))
numero_3 = int(input("Digite o terceiro número:"))
if numero_1 > numero_2:
  maior_numero = numero_1
elif numero_2 > numero_3:
  maior_numero = numero_2
else: maior_numero = numero_3

print("O maior número é:", maior_numero)
