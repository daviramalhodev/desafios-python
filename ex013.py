salario= float(input('Digite seu salario: R$ '))
new_salario= salario + (salario * 15 / 100)

print(f'Seu salario atual é de R$ {salario:.2f} reais!')
print(f'Com o aumento de 15%, seu novo salario será de R$ {new_salario:.2f} reais')