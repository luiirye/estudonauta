'''
Faça um programa que leia 5 valores numéricos e guarde-os numa lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas POSIÇÕES na lista
'''
lista_numeros = [] # inicia uma lista vazia
maior = menor = 0 # variáveis para armazenar o maior e menor número


for numero in range(0, 5):
    lista_numeros.append(int(input("Digite um número inteiro qualquer: "))) #append para adicionar elementos à lista
    print(f'Número {lista_numeros[numero]} adicionado á lista')

maior = max(lista_numeros)
menor = min(lista_numeros)

print(f'O maior número é {maior} na posição {lista_numeros.index(maior)}') # index para identificar a posição do número na lista
print(f'O menor número é {menor} na posição {lista_numeros.index(menor)}') # index para identificar a posição do número na lista