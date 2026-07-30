num1 = int(input("Qual o primeiro valor: "))
num2 = int(input("Qual o segundo valor: "))
opcao = 0
while opcao != 5:
    print('-=' * 10)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair')
    print('-=' * 10)
    opcao = int(input("Qual a sua opcao: "))
    if opcao == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif opcao == 2:
        multiplicar = num1 * num2
        print(f'{num1} * {num2} = {multiplicar}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num1 < num2:
            print(f'{num2} é maior {num1}')
        else:
            print(f'{num1} é igual a {num2}')
    elif opcao == 4:
        num1 = int(input("Qual o primeiro valor: "))
        num2 = int(input("Qual o segundo valor: "))
    elif opcao == 5:
        print('Sair')
    else:
        print('Digite uma opção valida!!!')
print('Fim do programa')