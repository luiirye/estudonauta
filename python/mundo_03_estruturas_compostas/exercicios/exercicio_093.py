'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois, vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols durante o campeonato.
'''
gols = list()
jogador = dict()
soma = 0

jogador ['nome'] = str(input(f'Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
jogador['partidas'] = partidas

for i in range(partidas):
    gols.append(int(input(f'Quantos gols {jogador['nome']} fez no {i + 1}º jogo? ')))
    soma += gols[i]
    jogador['gols'] = gols[:]

jogador['total'] = soma

print(jogador)

print(f'-=' * 30)
print(f'<== FICHA DO JOGADOR ==>')
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']}.')
for i in range(len(gols)):
    print(f'    => Na partida {i + 1}, fez {jogador['gols'][i]} gols.')
print(f'Com um total de {jogador['total']} gols.')