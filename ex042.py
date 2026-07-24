r1 = int(input("Digite o tamanho da primeira linha: "))
r2 = int(input("Digite o tamanho da segunda linha: "))
r3 = int(input("Digite o tamanho da terceira linha: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses 3 valores podem formar um triangulo")

    if r1 == r2 == r3:
        print("Como são valores iguais esse Triangulo vai ser EQUILATERO")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("Triangulo ESOSCELES, pois 2 lados são iguais!")
    else:
        print("Como nem um dos lados são iguais, esse é um triangulo ESCALENO")

else:
    print("Com esses valores não e possivel formar um triangulo")
