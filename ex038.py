num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

if num1 < num2:
    print(f"O segundo numero {num2} é maior que o primeiro numero {num1}: ")
elif num1 > num2:
    print(f"O primeiro numero {num1} é maior que o segundo numero {num2}: ")
else:
    print(f"Os dois numero são iguais {num1} = {num2}")