'''
Faça um programa que leia 5 valores numéricos e guarde-os numa lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas POSIÇÕES na lista
'''
lista_numeros = [] # inicia uma lista vazia
maior = menor = 0 # variáveis para armazenar o maior e menor número


for numero in range(0, 5):
    lista_numeros.append(int(input(f"Digite um valor para a posição {numero}: "))) #append para adicionar elementos à lista
    if numero ==  0:
        maior = menor = lista_numeros[numero]
    else:
        if lista_numeros[numero] > maior:
            maior = lista_numeros[numero]
        if lista_numeros[numero] < menor:
            menor = lista_numeros[numero]


print(f'O maior número é {maior} na posição {lista_numeros.index(maior)}') # index para identificar a posição do número na lista
print(f'O menor número é {menor} na posição {lista_numeros.index(menor)}') # index para identificar a posição do número na lista