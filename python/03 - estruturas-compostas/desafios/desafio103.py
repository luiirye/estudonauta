'''
faça um programa que tenha uma função chamada ficha().
Ficha() vai receber dois parâmetros opcionais: o nome de um jogador e quantos gols ele fez.

O Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(nome = 'Desconhecido', gols = 0):
    print(f'{nome} fez {gols} gols nesta temporada')
    
while True:
    
    
    
    resposta = ''
    resposta = str((input(f'Quer continuar? [S/N] ')))
    if resposta in 'Nn':
        print(f'Volte sempre!')
        break