valor_casa = float(input("Digite o valor da casa em R$: "))
salario = float(input("Digite o seu salario em R$: "))
parcela = int(input("Digite em quantas vezes você quer pagar: "))

analise = salario * 0.30
valor_parcela = valor_casa / parcela
print(f"30% = {analise}")
print(valor_parcela)

if valor_parcela <= analise:
    print(f"""
    =========  FINANCEIRO  =========
    APROVADO
    
    VALOR DA CASA:     R$ {valor_casa:.2f}
    FINANCIAMENTO EM:     {parcela}x
    VALOR DA PARCELA:  R$ {valor_parcela:.2f}
    ================================
    """)
elif valor_parcela > analise:
    print(f"""
        =========  FINANCEIRO  =========
        REPROVADO

        VALOR DA CASA:     R$ {valor_casa:.2f}
        FINANCIAMENTO EM:     {parcela}x
        VALOR DA PARCELA:  R$ {valor_parcela:.2f}
        ================================
        """)
