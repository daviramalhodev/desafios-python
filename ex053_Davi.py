frase = str(input("Digite uma frase: "))
frase_analise = frase.replace(" ", "")
frase_invertida = frase_analise[::-1]
analise = 0

if frase_invertida == frase_analise:
    print(f"""A frase {frase} de tras pra frente fica {frase_invertida}
Por tanto ela é um PALINDROMO""")
else:
    print(f"{frase} Não é um PALINDROMO")