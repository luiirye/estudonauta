time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input(f'Nome do Jogador: '))
    
    total = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        resposta = str(input(f'Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resposta == 'N':
        break
print(f'-=' * 30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print(f'-' * 40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()    
print(f'-' * 40)

while True:
    busca = int(input(f'Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print(f'<< VOLTE SEMPRE >>')