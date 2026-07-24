peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.1f} e esta ABAIXO DO PESO NORMAL")
elif imc < 25:
    print(f"Seu IMC é {imc:.1f} e esta IDEAL")
elif imc <= 30:
    print(f"Seu IMC é {imc:.1f} e esta SOBREPESO")
elif imc <= 40:
    print(f"Seu IMC é {imc:.1f} e esta com OBESIDADE")
else:
    print(f"Seu IMC é {imc:.1f} e esta com OBESIDADE MORBIDA")