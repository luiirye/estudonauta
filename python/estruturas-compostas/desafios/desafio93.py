'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois, vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols durante o campeonato.
'''
jogador= {} # dicionário para jogador
jogadores = [] # lista que vai armazenar todos os dicionários (cada jogador)

while True:
    
    jogador['nome'] = str(input(f'Nome: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    jogador['gols'] = int(input(f'Quantos gols {jogador['nome']} marcou? '))
    jogadores.append(jogador.copy())
    
    resposta = ''
    resposta = str(input(f'Quer continuar? [S/N] '))
    
    if resposta in 'Nn':
        break
    
print(jogadores)