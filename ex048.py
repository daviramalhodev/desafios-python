print("Numeros impares multiplos de 3:" )
soma = 0 #Exeplo de um acumulador
contador = 0 #Acumulador pra contagem
for c in range(3, 501, 2):
    if c % 3 == 0:
        contador = contador + 1 #Sempre achar um numero multiplo de 3 ele vai contar + 1 pra o contador
        soma += c
print()
print(f"A soma dos {contador} números solicitados é {soma}!")