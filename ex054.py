from datetime import date
from plyer import notification

menor = 0
maior = 0
ano_atual = date.today().year
for c in range(1, 8):
    nascimento = int(input(f"Digite o ano de nascimento da {c}° pessoa: "))
    if ano_atual - nascimento >= 18:
        maior += 1
    else:
        menor += 1

#Usei uma amneira diferente para mostrar uma noficação em vez de uma mensagem no console!
notification.notify(
    title="Resultado do desafio 54",
    message = f"""{maior} são Maiores de Idade
{menor} são Menor de Idade""",
    timeout = 10
)