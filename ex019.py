import random

a1= input('Qual o a1? ')
a2= input('Qual o a2? ')
a3= input('Qual o a3? ')
a4= input('Qual o a4? ')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print(f'O aluno sorteado foi {escolhido}')