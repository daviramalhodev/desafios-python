analise = []
for c in range(1, 6):
    peso = float(input("Digite o seu peso: "))
    analise.append(peso)
print(f"{max(analise)} é o Maior Peso\n {min(analise)} é o Menor peso!")
