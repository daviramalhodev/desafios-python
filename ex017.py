from math import pow, sqrt
cat_oposto = float(input('Digite o tamanho do cateto oposto: '))
cat_adjacente = float(input('Digite o tamanho do cateto adjacente: '))
hipotenusa = sqrt((pow(cat_oposto, 2)) + (pow(cat_adjacente, 2)))

print(f' A hipotenusa do triangulo retângulo é igual a {hipotenusa:.2f}')