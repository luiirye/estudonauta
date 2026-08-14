# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep

print("-=-" * 20)
print("Jogo da advinhação. Tente advinhar um número entre 0 a 5")
print("-=-" * 20)

num = int(input("Escolha um número de 0 a 5: ")) # número informado pelo usuário
rnum =  randint(0, 5) # Gera um número aleatório de 0 a 5
print("PENSANDO EM UM NÚMERO...")
sleep(2)

if (num == rnum):
    print(
        "Parabéns, você acertou o número!!\nNúmero sorteado: {}".format(rnum)
    )
    print("-=-" * 20)
else:
    print(
        "Não foi dessa vez...\nSeu Número: {}\nNúmero esperado: {}".format(num, rnum)
    )
    print("-=-" * 20)