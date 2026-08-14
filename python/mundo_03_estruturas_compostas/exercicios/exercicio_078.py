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

print(f'=-' * 30)
print(f'Você digitou os valores: {lista_numeros}')
print(f'O maior valor digitado foi: {maior},  nas posições: ', end='')
for i, v in enumerate(lista_numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi: {menor}, nas posições: ', end='')
for j, v in enumerate(lista_numeros):
    if v == menor:
        print(f'{j}... ', end='')