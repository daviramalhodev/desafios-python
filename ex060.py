fac = 1
num = int(input('Digite um numero: '))
contador = num
print(f'{contador} ', end='')
while num > 0:
    fac = fac * num
    num = num - 1
    contador -= 1
    print(f'x {contador} ', end='')
print(f' = {fac}')