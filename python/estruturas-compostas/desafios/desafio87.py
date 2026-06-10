'''
Aprimore o desafio anterior, mostrando no final:

1 - A soma de todos os valores pares digitados.
2 - A soma dos valores da terceira coluna.
3 - O maior valor da segunda linha.
'''

matriz = list([[],[],[]]) # definindo matriz 3x3
soma = somaj = maior = 0

for i in range(0, 9):
    numero = int(input(f'Digite um número para o bloco {i + 1} da matriz: '))
    if i < 3:
        matriz[0].append(numero)        
    elif i > 5:
        matriz[2].append(numero)
    else:
        matriz[1].append(numero)
        
    if numero % 2 == 0:
        soma += numero        

print(f'-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:3}] ', end = '')
    print()
print(f'-=' * 30)

print()

print(f'-=' * 30)

print(f'Soma de TODOS os números pares: {soma}')

for i in range(len(matriz)):
    somaj += matriz[i][2]
print(f'Soma dos valores da TERCEIRA COLUNA: {somaj}')

if matriz[1][0] > matriz[1][1]:
    maior = matriz[1][0]
elif matriz[1][1] > matriz[1][2]:
    maior = matriz[1][1]
else:
    maior = matriz[1][2]
print(f'O maior valor da segunda coluna é: {maior}')    

print(f'-=' * 30)