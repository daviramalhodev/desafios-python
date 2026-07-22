valor = int(input('Digite um número: '))

print('A tabuada de {} é:'.format(valor))
print('--------------')

for i in range(1, 11):
    print('{} x {} = {}'.format(valor, i, valor * i))

print('--------------')