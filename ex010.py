real= float(input('Quanto voce tem na carteira? R$'))
dolar= real/5.55

print(f'Com R$ {real} reais da para comprar $ {dolar:.2f} dolares')

# {dolar:.2f} mostra apenas duas casas apos o ponto, exemplo: $6.8789 para $6.08 deixando algo visualmente melhor