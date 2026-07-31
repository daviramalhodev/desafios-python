n = int(input('Digite um numero: '))
r = int(input('Digite sua razão: '))
total = 0
c = 1
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(n, end=" -> ")
        n += r
        c += 1
    print("PAUSA")
    mais = int(input('Quantos termos voce quer ver mais? [ 0 ] Pra encerrar! '))
print("FIM")
