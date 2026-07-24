nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
not

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 5:
    print(f"Sua média foi {media}, sendo assim está reprovado! ")
elif media >= 5 and media <= 6.9:
    print(f"Sua media foi {media} nesse caso vai precisar realizar a recuperação! ")
else:
    print(f"Parabéns sua media {media} então voce foi aprovado! ")