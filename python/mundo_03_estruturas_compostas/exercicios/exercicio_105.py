'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e retorne um dicionário com as seguintes informações;
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

Adicione também a docstrings da função.
'''
def linha():
    return print(f'==' * 15)

def notas(*n, sit=False):
    '''
    Função para registrar várias notas de uma turma.
    
    *n:
    - Inserir e agrupar incontáveis números.
    
    sit=False
    - Imprime a situação da turma (Reprovada ou Aprovada) caso verdadeiro. False por padrão.
    '''

    turma = {} # Iniciando um dicionário
    turma['Notas'] = n
    
    tamanho = len(turma['Notas'])
    turma['maior_nota'] = max(turma['Notas'])
    turma['menor_nota'] = min(turma['Notas'])
    turma['media_turma'] = (sum(turma['Notas']) / tamanho) 
    
    if turma['media_turma'] > 7:
        turma['situação'] = 'BOM'
    else:
        turma['situação'] = 'RUIM'
            
    if sit == True:
        print(f'Dicionário Completo: {turma}')
        print(f'Quantidade de notas: {tamanho}')
        print(f'Maior Nota: {turma['maior_nota']}')
        print(f'Menor Nota: {turma['menor_nota']}')
        print(f'Média da Turma: {turma['media_turma']}')
    else:
        del turma['situação']
        print(f'Dicionário completo: {turma}')
        print(f'Quantidade de notas: {tamanho}')
        print(f'Maior Nota: {turma['maior_nota']}')
        print(f'Menor Nota: {turma['menor_nota']}')
        print(f'Média da Turma: {turma['media_turma']}')
    
# Programa principal
notas(5,4,3,1,2,10,10,10, sit=False)
linha()
notas(5,4,3,1,2,10,10,10, sit=True)
linha()
notas(9,9,9,4,7, sit=True)
linha()
help(notas)