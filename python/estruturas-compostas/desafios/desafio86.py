'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a MATRIZ na tela, com a formatação correta.
'''
matriz = list([[],[],[]]) # definindo matriz 3x3

for i in range(0, 9):
    numero = int(input(f'Digite um número para o bloco {i + 1} da matriz: '))
    if i < 3:
        matriz[0].append(numero)        
    elif i > 5:
        matriz[2].append(numero)
    else:
        matriz[1].append(numero)    

print(f'-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:3}] ', end = '')
    print()
print(f'-=' * 30)