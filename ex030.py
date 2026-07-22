from ctypes import HRESULT

print("-=-" * 17)
print("   Digite um numero e veja se ele é PAR ou IMPAR: ")
print("-=-" * 17)

#numero = input("Digite um numero: ")
#if not numero.isdigit():
    #print("Digite apenas numero! ")
#else:
    #if  numero[-1] in ("0","2","4","6","8"):
        #print("É um numero PAR! ")
    #else:
        #print ("É um numero IMPAR! ")

#Outra opção simples:

numero = int(input("Digite um numero: "))
resultado = numero % 2

if resultado == 0:
    print("É um numero PAR! ")
else:
    print("É um numero IMPAR! ")