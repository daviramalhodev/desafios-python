from time import sleep
print(10 * "-=")
print("Contagem Regressiva")
print(10 * "-=")
segundos = int(input("Digite os segundos: "))

for c in range(segundos, -1, -1):
    print(f"\rContando: {c}", end="")
    sleep(1)
print()
print("Fogos de Artificio")