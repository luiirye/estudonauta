'''
Faça um programa que tenha uma função chamada contador().
Contador recebe 3 parâmetros: início, fim e passo, e realiza uma contagem.

Seu programa tem que realizar três contagens através da função criada.

A) de 1 até 10, de 1 em 1.
B) de 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
'''
from time import sleep

def contador(inicio, fim, passo):

    for inicio in range(fim):
        inicio += passo
        print(inicio, end = ' ')
        
contador(1, 10, 1)
contador(10, 0, 2)
contador(3,30,10)