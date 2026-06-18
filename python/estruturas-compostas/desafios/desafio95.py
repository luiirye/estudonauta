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
gols = list() # lista para armazenar os gols
gols_soma = 0

while True:
    
    nome = str(input(f'Nome: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols {nome} fez na {i + 1}ª partida? '))) 
        gols_soma += gols[i]
        
    # adicionando ao dicionário
    jogador['nome'] = nome
    jogador['partidas'] = partidas
    jogador['gols'] = gols[:]
    jogador['total'] = gols_soma
    
    jogadores.append(jogador.copy())
    
    gols.clear()
    gols_soma = 0
    
    resposta = ''
    resposta = str(input(f'Quer continuar? [S/N] '))
    
    if resposta in 'Nn':
        break
        
print(f'-=' * 30)
print(f'<========== FICHA DE JOGADORES ==========>')
print(f'-=' * 30)
print(f'Total de jogadores: {len(jogadores)}\nTabela de Jogadores: ')

for i in range(len(jogadores)):
    print(f'{i + 1} - {jogadores[i]['nome']}')
    
while True:

    resposta = ''
    resposta = str(input(f'Gostaria de ver as estatísticas de algum jogador da tabela? [S/N] '))
    opt = 0
    if resposta in 'Ss':
        print(f'-=' * 30)
        opt = int(input('Informe o número do jogador na tabela: '))
        print(f'Ficha de {jogadores[opt - 1]['nome']}')
        print(f'Partidas jogadas: {jogadores[opt - 1]['partidas']}')
        print(f'Gols: {jogadores[opt - 1]['gols']}')
        print(f'Total de gols: {jogadores[opt - 1]['total']}')
                 
    elif resposta in 'Nn':
        break
print(f'<========== ATÉ MAIS ==========>')