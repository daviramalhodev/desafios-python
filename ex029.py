velocidade = float(input("Digite qual a velocidade em km/h: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"{velocidade} km/h | Velocidade acima da permitida, você sera multado em R$ {multa} reais")
else:
    print (f"{velocidade} km/h está dentro do permitido! ")