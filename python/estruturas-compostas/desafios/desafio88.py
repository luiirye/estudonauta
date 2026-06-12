'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar QUANTOS JOGOS serão gerados e vai serotear 6 númeores entre 1 e 60, para cada jogo.
Cadastre tudo em uma lista composta.
'''

from random import randint # Para gerar os números aleatórios
from time import sleep 

jogos = list() # Gera uma lista vazia

print(f'-' * 30)
print(f'JOGA NA MEGA SENA QUE É SUCESSO!')
print(f'-' * 30)

palpites = int(input(f'Quantos jogos quer que eu sorteie? '))

print(f'Sorteando {palpites} jogos')

for i in range(palpites):
    jogos.append(list())

print(jogos)

for j in range(palpites):
    
    for l in range(0,6):
        jogos[j].append(randint(1, 60))
        jogos[j].sort()


        
    
for k in range(len(jogos)):
    print(f'Jogo {k + 1:2} : {jogos[k]}')
    ##sleep()
    
print(f'BOA SORTE!!')
    