analise = 0
while analise == 0:
    sexo = str(input("Sexo [M/F]: ")).upper()
    if sexo == 'M':
        analise += 1
    if sexo == 'F':
        analise += 1

print(f"Sexo {sexo}")