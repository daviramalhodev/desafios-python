while True: #cria um loop ate o usuario digitar apenas numeros
    num = input("Digite um numero de 4 digitos: ").strip()
    if num.isdigit(): #verifica se é apenas numeros
        break #se for apenas numero o loop encerra e segue o codigo
    else:
        print("Só é permitido numeros, digite novamente!")

numf = num.zfill(4) #Faz com que preencha de 0 a esquerda ate ficar com 4 digitos
# se digitar 25, vai transoformar 0025
cen = numf[1]
dez = numf[2]
mil = numf[0]

if int(num) < 10:
    dez = "Não Tem"

if int(num) < 100:
    cen = "Não tem"

if int(num) <1000:
    mil = "Não tem"

print(f"""Unidade: {numf[3]}
Dezena:  {dez}
Centena: {cen}
Milha:   {mil}""")