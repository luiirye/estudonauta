'''
Faça um programa que tenha uma função chamada contador().
Contador recebe 3 parâmetros: início, fim e passo, e realiza uma contagem.

Seu programa tem que realizar três contagens através da função criada.

A) de 1 até 10, de 1 em 1.
B) de 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
'''
from time import sleep

def contador(i, f, p):
    # Trata o passo caso seja 0
    if p == 0:
        p = 1
    
    # Exibe a mensagem de início da contagem
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    
    # Trata o passo caso seja negativo (contagem regressiva)
    if p < 0:
        p = abs(p)
        
    # Realiza a contagem progressiva
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
    
    # Realiza a contagem regressiva
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
    print('FIM!')

# a) Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# b) Contagem de 10 até 0, de 2 em 2
contador(10, 0, 2)

# c) Contagem personalizada
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)
