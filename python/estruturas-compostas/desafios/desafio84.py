'''
Faça um programa que leia NOME E PESO  de VÁRIAS PESSOAS.
guardando tudo em uma LISTA. No final, mostre

1 - Quantas pessoas foram cadastradas.
2 - Uma listagem com as pessoas mais pesadas.
3 - Uma listagem com as pessoas mais leves.
'''
lista = list() # lista vazia
dado = list()
total_pessoas = menor = maior = 0

while True:
    
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    
    lista.append(dado[:])
    dado.clear() # Limpa a lista
    
    resposta = str(input(f'Quer continuar? [S/N] '))
    
    if resposta in 'Nn':
        print('Até mais...')
        break

print('-=' * 30)

for i in range(len(lista)):
    if lista[i][0]:
        total_pessoas += 1
print(f'Foram cadastradas {total_pessoas} pessoas na lista.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end = '')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end = '')
print()
print(f'O Menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa in lista:
    if pessoa [1] == menor:
        print(f'[{pessoa[0]}]', end='')
print()
print('-=' * 30)