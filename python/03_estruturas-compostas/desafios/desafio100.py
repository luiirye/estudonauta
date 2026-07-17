'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 NÚMEROS e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores Pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end = '', flush=True)
        sleep(0.3)
    print(f'PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()

sorteia(numeros)
somaPar(numeros)