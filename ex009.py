valor= int(input('Digite um numero: '))
contador = 1

print(f"A tabuada do numero {valor} é:")
print("------------")
while contador <= 10:
    print (f"{valor} x {contador:2} = {valor * contador} ")
    contador += 1
print("------------")