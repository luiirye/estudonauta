'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior da tupla
'''
from random import randint

maior = 0
menor = 0
# gera 5 números inteiros de 1 a 50 e armazena na tupla
numeros = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))

print('-' * 45)
print(f"Listagem dos números: {numeros}")
print('-' * 45)

print(f'menor: {min(numeros)}')
print(f'maior: {max(numeros)}')