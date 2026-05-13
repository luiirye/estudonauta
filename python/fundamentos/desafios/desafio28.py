# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint

num = int(input("Escolha um número de 1 a 5: "))
rnum =  randint(1, 5) # Gera um número aleatório de 1 a 5

if (num == rnum):
    print(
        "Parabéns, você acertou o número!!\nNúmero sorteado: {}".format(rnum)
    )
else:
    print(
        "Não foi dessa vez...\nSeu Número: {}\nNúmero esperado:{}".format(num, rnum)
    )