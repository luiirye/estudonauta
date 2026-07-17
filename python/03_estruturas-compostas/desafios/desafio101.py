'''
Crie uma função chamada voto().
Voto() vai receber o ano de nascimento de uma pessoa.
A função deve retornar um valor literal, indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
def voto(ano_nascimento = 0):
    
    from datetime import datetime
    
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16 :
        return f'com {idade} anos: NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: OPCIONAL'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'
    
while True:
    ano = int(input(f'Ano de nascimento: '))
        
    print(voto(ano))
        
    resposta = ''
    resposta = str(input(f'Quer continuar? [S/N] '))
    if resposta in 'Nn':
        print(f'Volte sempre!')
        break

