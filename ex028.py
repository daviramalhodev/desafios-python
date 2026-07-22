import random
import time

num_pc = random.randint(0, 5)

num = input("Adivinhe qual numero eu estou pensando, entre 0 e 5: ")
print("So um momento enquanto verifico....")

time.sleep(2) #adiciona uma pausa ate continuar o codigo!!

print(f"Numero que pensei {num_pc}")
print(f"Numero que voce digitou {num}")

if int(num) == num_pc:
    print(f"Parabens voce acertou")
else:
    print("Que pena voce errou!!")

