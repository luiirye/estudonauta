'''
faça um programa que tenha uma função chamada ficha().
Ficha() vai receber dois parâmetros opcionais: o nome de um jogador e quantos gols ele fez.

O Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(nome_jogador = 'Desconhecido', gols = 0):
    return print(f'{nome_jogador} fez {gols} gols')

while True:
    
    nome = str(input(f'Nome: '))
    gols = str(input(f'Gols: '))
    
    if nome == '':
        nome = 'Desconhecido'
    if gols == '':
        gols = 0
    else:
        gols = int(gols)
    
    ficha(nome, gols)
    
    resp = ''
    resp = str(input(f'Quer continuar? [S/N] '))
    if resp in 'Nn':
        print(f'Saindo...')
        break