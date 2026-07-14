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
    maior_nota = max(turma['Notas'])
    menor_nota = min(turma['Notas'])
    media_turma = (sum(turma['Notas']) / tamanho) 
        
    print(f'Dicionário Completo: {turma}')
    print(f'Quantidade de notas: {tamanho}')
    print(f'Maior Nota: {maior_nota}')
    print(f'Menor Nota: {menor_nota}')
    print(f'Média da Turma: {media_turma}')
    
    if sit == True:
        if media_turma > 7:
            return print(f'Turma Aprovada!!')
        else:
            return print(f'Turma Reprovada!')

# Programa principal

notas(5,4,3,1,2,10,10,10, sit=False)
linha()
notas(5,4,3,1,2,10,10,10, sit=True)
linha()
notas(9,9,9,4,7, sit=True)