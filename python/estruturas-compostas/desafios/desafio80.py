'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção(sem usar o sort()).

No final, mostre a listsa ordenada na tela.
'''
numeros = [] # Lista vazia

for num in range(0, 5):
    num = int(input("Digite um número para adicionar na lista: "))
    numeros.append(num)

print(f"Lista completa (Desordenada): {numeros}")

tamanho = len(numeros)

for i in range(tamanho - 1):
    for j in range(tamanho - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Trocando elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
## Ordenando
print(f'Lista de números ordenadas: {numeros}')

            
            