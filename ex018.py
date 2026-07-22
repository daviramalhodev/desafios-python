import math
ang = float(input('Digite um angulo em graus: '))
ang_graus = math.radians(ang)

print(f'O angulo fornecido é {ang}')
print(f'Seu seno é igual {math.sin(ang_graus):.2f}')
print(f'Seu cosseno é igual {math.cos(ang_graus):.2f}')
print(f'E sua tangente é igual a {math.tan(ang_graus):.2f}')
