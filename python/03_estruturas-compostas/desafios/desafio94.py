'''
Crie um programa que leia NOME, SEXO e IDADE de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
- A) Quantas pessoas foram cadastradas
- B) A Média de idade do grupo
- C) Uma lista com todas as mulheres
- D) UMa lista com todas as pessoas com idade acima da média
'''
# variáveis para o exercício
totp = 0
medid = 0
listMulheres = []
listPessoasAcima = []
pessoa = dict()
pessoas = list()

while True:
    
    nome = str(input(f'Nome: '))
    sexo = str(input(f'Sexo de {nome}: ')).upper().strip()[0]
    idade = int(input(f'Idade de {nome}: '))
    
    totp += 1 # Uma pessoa cadastrada
    medid += idade
    
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    
    # cada pessoa é sobrescrita após rodar o loop mais uma vez e inserindo novas informações
    # Por isso, fiz uma cópia de cada dicionário em uma lista.
    if pessoa['sexo'] == 'F':
        listMulheres.append(pessoa['nome'])
        
    if pessoa['idade'] > medid:
        listPessoasAcima.append(pessoa['nome'])
    
    pessoas.append(pessoa.copy())
            
    resposta = ''
    resposta = str(input(f'Quer continuar? [S/N] '))
    print('-=' * 30)
    
    if resposta in 'Nn':
        break
    
print(f'A) Ao todo foram cadastradas {totp} pessoas.')
print(f'B) A Média de idade é de {medid:.2f} anos.')
print(f'C) Mulheres Cadastradas: ')
for mulher in listMulheres:
    print(f'    => {mulher}')
    
print(f'D) Lista de pessoas que estão acima da média: ')
for pessoa in listPessoasAcima:
    print(f'    => {pessoa}')