salario = float(input("Qual o seu salario em R$: "))

if salario <= 1250:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10

print(novo_salario)