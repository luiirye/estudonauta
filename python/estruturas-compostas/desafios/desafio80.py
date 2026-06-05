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


'''
Entendo o algorimto.
Criado uma variável "tamanho" para guardar o tamanho da lista e ficar mais fácil de utilizar na ordenação.
Algoritmo chamado de "bubble sort".

O que ele faz?
o - 1 serve para que o J acesse até o penúltimo índice, sem quebrar o código, assim chegando na condição do "if", ele consegue acessar o últi em j + 1. 
o trecho  com -i serve para ir "empurrando" o número ordenado para o fim da lista

'''

print(f'Lista de números ordenadas: {numeros}')

            
            