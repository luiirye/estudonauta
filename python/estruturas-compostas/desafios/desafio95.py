'''
desafio 93

Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois, vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols durante o campeonato.

Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 
'''
# Variáveis 
jogador = dict() # cadastra UM jogador
jogadores = list() # guarda TODOS os jogadores cadastrados em jogador
gols = 0 # variável para armazenar os gols
gols_soma = 0

while True:
    
    nome = str(input(f'Nome: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    
    for gol in range(partidas):
        gols = int(input(f'Quantos gols {nome} fez na {gol + 1}ª partida? '))
        gols_soma += gols
    
    # Adicionando as informações em um dicionário
    
    jogador[]
    jogador[]
    jogador[]
    jogador[]
    
    resposta = ''
    resposta = str(input(f'Quer continuar? [S/N] '))
    
    if resposta in 'Nn':
        break
        
print()