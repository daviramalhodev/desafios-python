from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

#print(f"O COMPUTADOR escolheu {itens[computador]}")
print("""Suas Opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Escolha sua opção: "))

if jogador <0 or jogador > 2:
    print("Jogada Invalida, Escolha 0, 1 ou 2!!!")
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-='*13)
    print(f"O COMPUTADOR escolheu {itens[computador]}")
    print(f"O JOGADOR escolheu {itens[jogador]}")
    print('-='*13)

    if jogador == 0 and computador == 2 or \
        jogador == 1 and computador == 0 or \
        jogador == 2 and computador == 1:
        print("VOCE VENCEU")

    elif jogador == 0 and computador == 1 or \
        jogador == 1 and computador == 2 or \
        jogador == 2 and computador == 0:
        print("VOCE PERDEU")

    else:
        print("EMPATOU")

