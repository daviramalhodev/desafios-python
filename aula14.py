c = 1
pares = 0
impares = 0
while c != 0:
    c = int(input("Numero: "))
    if c % 2 == 0 and c != 0:
        pares += 1
    else:
       impares += 1
print(f"{pares} Pares")
print(f"{impares} Impares")



