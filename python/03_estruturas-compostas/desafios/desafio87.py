'''
Aprimore o desafio anterior, mostrando no final:

1 - A soma de todos os valores pares digitados.
2 - A soma dos valores da terceira coluna.
3 - O maior valor da segunda linha.
'''

matriz = list([[0,0,0],[0,0,0],[0,0,0]]) # definindo matriz 3x3
soma = somaj = maior = 0

for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

print('-=' * 30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'-=' * 30)

print()

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

print()

print(f'-=' * 30)