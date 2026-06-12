'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar QUANTOS JOGOS serão gerados e vai serotear 6 númeores entre 1 e 60, para cada jogo.
Cadastre tudo em uma lista composta.
'''

from random import randint # Para gerar os números aleatórios
from time import sleep 

jogos = list() # Gera uma lista vazia

print(f'-' * 50)
print(f'JOGA NA MEGA SENA QUE É SUCESSO!')
print(f'-' * 50)

palpites = int(input(f'Quantos jogos quer que eu sorteie? '))
print(f'-' * 50)

print(f'Sorteando {palpites} jogos')
print(f'-' * 50)

for i in range(palpites):
    jogos.append(list())

for j in range(palpites):
    for l in range(0,6):
        jogos[j].append(randint(1, 60))
        jogos[j].sort()

for k in range(len(jogos)):
    print(f'Sorteando jogo {k + 1}...')
    sleep(0.5)
    print(f'Jogo {k + 1:2} : {jogos[k]}')
    sleep(0.5)

print(f'-' * 50)    
print(f'Números sorteados para {palpites} jogos!!')

print(f'-' * 50)
print(f'BOA SORTE!!')
print(f'-' * 50)