import random

num_pc = random.randint(0,10)
contador = 1
print('-=' * 11)
print('= ADIVINHE O NUMERO  =')
print('-=' * 11)
num_usuario = int(input('Diga um numero entre 0 e 10: '))

while num_pc != num_usuario:
    if  num_usuario < num_pc:
        num_usuario = int(input('Mais um pouco!!! Tente novamente: '))
    else:
        num_usuario = int(input('Menos um pouco!!! Tente novamente: '))
    contador += 1
print("-=" * 15)
print(f'Voce acertou depois de {contador} vezes')
print("-=" * 15)