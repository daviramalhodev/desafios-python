n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo  numero:"))
n3 = int(input("Digite o terceiro numero:"))
"""if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior numero")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior numero")
else:
    print(f"{n3} é o maior numero")

print(f"Numero 1: {n1}, Numero 2: {n2} e Numero 3: {n3}")"""

maior = n1

if n2 >= maior:
    maior = n2
if n3 >= maior:
    maior = n3

menor = n1

if n2 <= menor:
    menor = n2
if n3 <= menor:
    menor = n3

print(f" o MAIOR numero é {maior}")
print(f" o MENOR numero é {menor}")