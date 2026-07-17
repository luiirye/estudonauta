'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados ALEATÓRIOS.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou O MAIOR NÚMERO no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}

print(' == JOGANDO DADOS == ')
for chave, valor in jogo.items():
    print(f'{chave} tirou o {valor} no dado.')
    sleep(1)
    
ranking = list()

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'-=' * 30)
print(f' == RANKING DOS JOGADORES == ')
for i, valor in enumerate(ranking):
    print(f'- {i + 1}º Lugar: {valor[0]} com {valor[1]}')
    sleep(1)
print()