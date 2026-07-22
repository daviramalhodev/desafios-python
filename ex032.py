ano = int(input("Qual o ano que voce quer avaliar: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f" ano de {ano} é BISSEXTO!")
else:
    print(f"O ano de {ano} NÃO é BISSEXTO")