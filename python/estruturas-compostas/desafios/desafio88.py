'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar QUANTOS JOGOS serão gerados e vai serotear 6 númeores entre 1 e 60, para cada jogo.
Cadastre tudo em uma lista composta.
'''
palpites = [] # lista para palpites.

while True:
    
    quantidade_jogos = int(input('Quantos jogos serão gerados? [Lembrete: cada jogo terá 6 números] '))
    
    for i in range(quantidade_jogos):
        jogos = list()
    
    palpites.append(jogos)
    break

print(palpites)
    
    