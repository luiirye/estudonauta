'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 NÚMEROS e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores Pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    
    lista = list()
    
    for i in range(0,5):
        num = randint(1,10)
        lista.append(num)
        sleep(0.5)
    
    print(f'Números sortados: ')
    for j in range(len(lista)):
        print(f'{lista[j]}', end= ' ', flush = True)    
    
def somaPar(lista):
    
    soma = 0
    
    for i in lista:
        if i % 2 == 0:
            print(f'Números Pares: {lista[i]}')
            soma += i
        
    print(f'A soma dos pares é {soma}')    


sorteia(numeros)
print()
somaPar(numeros)