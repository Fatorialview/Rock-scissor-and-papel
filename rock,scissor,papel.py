#ROCK, SCISSOR AND PAPER
import random

print("Escolha: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n")


escolha = int(input("Escolha:"))
cpu = random.randint(1, 3)

if escolha == cpu:
    print("Empate")
elif escolha == 1:
        if cpu == 2:
            print("Papel. CPU Venceu!")
        else:
            print("Tesoura. Você Venceu!")
elif escolha == 2:
        if cpu == 1:
            print("Pedra. Você Venceu!")
        else:
            print("Tesoura, CPU Venceu!")
elif escolha == 3:
            if cpu == 1:
                print("Pedra. CPU Venceu!")
            else:
                print("Pedra. Você Venceu!")

       