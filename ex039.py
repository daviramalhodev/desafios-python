from datetime import date
ano_nasciemnto = int(input("Digite o ano que você nasceu: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasciemnto
print(f"Sua idade é {idade}")

dif = idade - 18
if idade == 18:
    print("Está na hora de se alistar")
elif idade < 18:
    print("Ainda não está na hora de se alistar")
else:
    print(f"Vá o quanto antes, \n pois já deveria ter se alistado a {dif} anos!!!")