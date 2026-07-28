numero = int(input("Digite um numero: "))
contador = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        contador += 1
if contador == 2:
    print(f"{numero} é PRIMO!")
else:
    print(f"{numero}  Não é PRIMO")

