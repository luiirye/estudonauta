'''
Faça um programa que leia NOME E MÉDIA de um aluno.
Guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict() # Declaração do dicionário
aluno['nome'] = str(input(f'Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

# Verificação de situação
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print(f'-=' * 40)
for key, value in aluno.items():
    print(f' -  {key} é igual a {value} ')
print(f'-=' * 40)