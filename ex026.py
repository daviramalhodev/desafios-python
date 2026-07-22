entrada = input("Digite uma frase : ").upper().strip()

ca = entrada.count("A")
fa = entrada.find("A")
rf = entrada.rfind("A")

print(f"""Sua frase contem: {ca} A
O primeiro A aprece na posição: {fa}
O ultimo A aparece na posição: {rf}""")

