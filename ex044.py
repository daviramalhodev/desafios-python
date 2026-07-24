valor_produto = float(input("Digite o valor do produto: R$ "))
forma_pagamento = input(
"""Em qual forma de pagamento?
-------------------------
[ 1 ] À dinheiro ou cheque
[ 2 ] À vista cartão 
[ 3 ] Em ate 2x cartão
[ 4 ] Em 3x ou mais cartão
""")

if forma_pagamento == "1":
    valor_produto = valor_produto * 0.90
    print(f"Com o desconto vai sair por R${valor_produto:.2f}")
elif forma_pagamento == "2":
    valor_produto = valor_produto * 0.95
    print(f"Com o desconto vai sair por R${valor_produto:.2f}")
elif forma_pagamento == "3":
    valor_produto = valor_produto / 2
    print(f"Nesse caso fica 2x de R$ {valor_produto:.2f} sem juros")
else:
    valor_produto = valor_produto * 1.20
    print(f"""
Acima de 3x tem juros de 20%
----------------------------
3x de R$ {valor_produto / 3:.2f}
4x de R$ {valor_produto / 4:.2f}
5x de R$ {valor_produto / 5:.2f}
6x de R$ {valor_produto / 6:.2f}
7x de R$ {valor_produto / 7:.2f}
8x de R$ {valor_produto / 8:.2f}
9x de R$ {valor_produto / 9:.2f}
10x de R$ {valor_produto / 10:.2f}

Valor total: R$ {valor_produto:.2f}
""")