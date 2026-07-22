nome = input("Digite seu nome completo: ")

print(f"seu nome é {nome.upper()} ?")
print(f"seu nome é {nome.lower()} ?")
print(f"seu nome tem {len(nome.replace(" ", ""))}  letras!")

pnome = nome.split()

print(f"Seu primeiro nome tem {len(pnome[0])} letras")