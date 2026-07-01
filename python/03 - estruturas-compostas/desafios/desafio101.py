'''
Crie uma função chamada voto().
Voto() vai receber o ano de nascimento de uma pessoa.
A função deve retornar um valor literal, indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
from datetime import datetime 

def voto(ano_nascimento = 0):
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16 :
        return "NEGADO"
    elif idade == 16 and idade == 17:
        return "OPCIONAL"
    elif idade > 18:
        return "OBRIGATÓRIO"
    
while True:
    
    ano = int(input(f'informe seu ano de nascimento: '))
    
    
    
    
    resposta = ''
    resposta = str(input(f'Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

