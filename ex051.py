num = int(input("Digite o numero inicial da PA: "))
razao = int(input("Digite a razão da PA: "))
soma = num
for c in range(1, 11):
    print(soma, end=" -> ")
    soma += razao
print("FIM")
