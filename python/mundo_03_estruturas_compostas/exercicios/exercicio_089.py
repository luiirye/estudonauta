'''
Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno INDIVIDUALMENTE.
'''
alunos = list()
nome = ''
nota1 = nota2 = cont_aluno = media = 0

while True:
    
    nome = str(input(f'Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    
    alunos.append(list())
    
    alunos[cont_aluno].append(nome)
    alunos[cont_aluno].append(nota1)
    alunos[cont_aluno].append(nota2)

    cont_aluno += 1
    
    resposta = str(input('Quer continuar? [S/N] '))
    
    if resposta in 'Nn':
        break

print(f'-=' * 30)
print("BOLETIM DOS ALUNOS")

for i in range(len(alunos)):
    print(f'-=' * 30)
    print(f'Boletim do {i + 1}º aluno:')
    print(f'Aluno : {alunos[i][0]}')
    # calculo das medias
    media = (alunos[i][1] + alunos[i][2]) / 2
    
    print(f'Média : {media:.1f}')

print()

while True:
    
    resp = str(input(f'Gostaria de exibir a nota individual de algum aluno? [S/N] '))
    
    if resp in 'Nn':
        break
    else:
        aluno = int(input(f'Qual aluno quer visualizar? [Números de alunos na lista: {len(alunos)}] '))
        print(f'-=' * 30)
        print(f'Aluno informado: {aluno}')
        print(f'Nome  : {alunos[aluno - 1][0]}')
        print(f'Nota 1: {alunos[aluno - 1][1]}')
        print(f'Nota 2: {alunos[aluno - 1][2]}')