while True:     
    num = int(input("Digite um valor inteiro: "))
    break
print(num)

print("Escolha qual conversão quer fazer!")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

op = int(input("Digite um numero: "))

if op == 1:
    print(bin(num)[2:])
elif op == 2:
    print(oct(num)[2:])
elif op == 3:
    print(hex(num))
else:
    print("Opção invalida!!!")