
fem_20 = 0
homem_velho = ""
soma_idade = 0
idade_homemvelho = 0

for c in range(1, 5):
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite o seu sexo [M/F]: "))
    soma_idade += idade
    if idade > idade_homemvelho and sexo == "M":
        idade_homemvelho = idade
        homem_velho = nome
    if sexo == "F" and idade < 20:
        fem_20 += 1

print(f"A media de idade do grupo é {soma_idade / 4}")
print(f"O homem mais velho do grupo se chama {homem_velho}")
print(f"O grupo tem {fem_20} mulheres com menos de 20 anos")
