'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados ALEATÓRIOS.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou O MAIOR NÚMERO no dado.
'''

from random import randint

jogadores = dict() # Criando o dicionário

# Adicionando jogadores ao dicionário
for i in range(0,4):
    jogadores[f"jogador{i}"] = randint(1,6)
    
    
print(jogadores) # Dicionário desordenado.