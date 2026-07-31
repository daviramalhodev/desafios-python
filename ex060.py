'''fac = 1
num = int(input('Digite um numero: '))
contador = num
print(f'{contador} ', end='')
while num > 1:
    fac = fac * num
    num = num - 1
    contador -= 1
    print(f'x {contador} ', end='')
print(f' = {fac}')'''

num = int(input('Digite um numero: '))
fac = 1

while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fac *= num
    num -= 1
print(fac)