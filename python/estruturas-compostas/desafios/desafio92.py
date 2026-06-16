'''
Crie um programa que leia NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO.
Cadastre-os (com idade) em um DICIONÁRIO.
Se por um acaso a CTPS for diferente de ZERO. O dicionário receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO.
Calcule e acrescente, além da IDADE, com quantos anos vai se aposentar.
Considere aposentadoria 35 anos de contribuição.
'''
from datetime import date
hoje = date.today().year
print(hoje)

trabalho = dict()
trabalho['nome'] = str(input(f'Nome: '))
trabalho['idade'] = int(input(f'Ano de nascimento: '))
trabalho['idade'] = (hoje - trabalho['idade'])
trabalho['ctps'] = int(input(f'Carteira de Trabalho (0 = Não tem): '))
if trabalho['ctps'] == 0:
     trabalho['ctps'] = 0
else:
    trabalho['contratacao'] = int(input(f'Ano de Contratação: '))
    trabalho['Salario'] = float(int(f'Salário: R$ '))
    
    
    
for chave, valor in trabalho.items():
    print(f'{chave} tem o valor {valor}')
