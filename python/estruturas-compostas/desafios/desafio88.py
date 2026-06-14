'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar QUANTOS JOGOS serão gerados e vai serotear 6 númeores entre 1 e 60, para cada jogo.
Cadastre tudo em uma lista composta.
'''

from random import randint # Para gerar os números aleatórios
from time import sleep 

lista = list()
jogos = list()

print(f'-' * 32)
print(f'        JOGA NA MEGA SENA       ')
print(f'-' * 32)

print()
quantidade = int(input(f'Quantos jogos você quer que eu sorteie? '))
total_jogos = 1

while total_jogos <= quantidade:
        
    cont = 0

    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos += 1

print()

print(f'-=' * 3, f'SORTEANDO {quantidade} JOGOS', f'-=' * 3)

for i, l, in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'-=' * 5, '< BOA SORTE! >', f'-=' * 5)
        