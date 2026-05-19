# Melhore o jogo desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Desafio 028 abaixo
from random import randint
from time import sleep

print("-=-" * 20)
print("Jogo da advinhação. Tente advinhar um número entre 0 a 10")
print("-=-" * 20)

num = 0
rnum = 1

palpites = 0 # Contador

while num != rnum:
    
    print("<===========================>")
    
    num = int(input("Escolha um número de 0 a 10: ")) # número informado pelo usuário
    rnum =  randint(0, 10) # Gera um número aleatório de 0 a 10
    
    print("Pensando.")
    sleep(0.5)
    print("Pensando..")
    sleep(0.5)
    print("Pensando...")
    
    palpites += 1
    
    if num != rnum:
        print("Você digitou {}.\nNumero sorteado: {}.\nNão foi dessa vez".format(num, rnum))
    else:
        print("PARABÉNS, VOCÊ ADVINHOU O NÚMERO!!\nNúmero digitado: {}\nNúmero sorteado: {}".format(num, rnum))
        print("Quantidades de palpites: {}".format(palpites))