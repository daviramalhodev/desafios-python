from random import randint

print("==== Pedra, Papel ou Tesoura ====")

print("""
        Escolha Uma Opção:
        ------------------
        [ 1 ] Pedra
        [ 2 ] Papel
        [ 3 ] Tesoura
        ------------------
        """)
escolha = int(input("Qual a sua escolha: "))
n_pc = randint(1, 3)
print(n_pc, escolha)

if n_pc == 1 and escolha == 2:
    print(f"""PC escolheu: PEDRA e Você escolheu: PAPEL
Você GANHOU""")

elif n_pc == 2 and escolha == 3:
    print(f"""PC escolheu: PAPEL e Você escolheu: TESOURA
Você GANHOU""")

elif n_pc == 3 and escolha == 1:
    print(f"""PC escolheu: TESOURA e Você escolheu: PEDRA
Você GANHOU""")

elif n_pc == 1 and escolha == 3:
    print(f"""PC escolheu: PEDRA e Você escolheu: TESOURA
Você PERDEU""")

elif n_pc == 2 and escolha == 1:
    print(f"""PC escolheu: PAPEL e Você escolheu: PEDRA
Você PERDEU""")

elif n_pc == 3 and escolha == 2:
    print(f"""PC escolheu: TESOURA e Você escolheu: PAPEL
Você PERDEU""")

else:
    print("EMPATOU, TENTE NOVAMENTE")