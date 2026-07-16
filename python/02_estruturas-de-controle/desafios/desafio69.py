'''
Crie um programa que leia a idade e o sexo de várias pessoas.

A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

No final, mostre:
    A) Quantas pessoas tem mais de 18 anos
    B) Quantos HOMENS foram cadastrados
    C) Quantas MULHERES tem menos de 20 anos
'''
tot18 = totH = totM20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')