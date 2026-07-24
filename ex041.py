from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual - ano_nascimento

print(f"""
O atleta nasceu em {ano_nascimento}
nesse caso o atleta tem {idade} anos.
""")

if idade <= 9:
    print(f"O atleta pertence a categoria MIRIM!")
elif idade <= 14:
    print(f"O atleta pertence a categoria INFANTIL!")
elif idade <= 19:
    print(f"O atleta pertence a categoria JUNIOR!")
elif idade <= 25:
    print(f"O atleta pertence a categoria SENIOR!")
else:
    print(f"O atleta pertence a categoria MASTER!")