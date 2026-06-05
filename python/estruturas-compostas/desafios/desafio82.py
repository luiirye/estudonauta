'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas
'''
# Listas vazias
numeros = []
pares = []
impares = []
tamanho = 0

while True:
    num = int(input("Digite um número para ser adicionado à lista: "))
    numeros.append(num)

    # Para em zero
    if num == 0:
        numeros.pop()
        break
    
tamanho = len(numeros)

for i in range(tamanho):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])

# Ordenados

numeros.sort()
pares.sort()
impares.sort()

print(f'Lista: {numeros}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')