'''
Faça um programa que leia NOME E PESO  de VÁRIAS PESSOAS.
guardando tudo em uma LISTA. No final, mostre

1 - Quantas pessoas foram cadastradas.
2 - Uma listagem com as pessoas mais pesadas.
3 - Uma listagem com as pessoas mais leves.
'''
lista = list() # lista vazia
dado = list()
total_pessoas = 0

while True:
    
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
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
print(f'Foram cadastradas {total_pessoas} pessoas na lista')

print('As pessoas mais pesadas da lista são: ', end = '')
for i in range(len(lista)):
    if lista[i][1] >= 100:
        print(f'{lista[i][0]}, ', end = '' )
        print(f'pesando {lista[i][1]}KG... ', end = '')

print() # quebrar linha

print('As pessoas mais leves da lista são: ', end = '')
for i in range(len(lista)):
    if lista[i][1] < 100:
        print(f'{lista[i][0]}, ', end = '' )
        print(f'pesando {lista[i][1]}KG... ', end = '')

print() # Quebra de linha
print('-=' * 30)