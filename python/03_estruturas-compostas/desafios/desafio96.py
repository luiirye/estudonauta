'''
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular.
dimensões: (largura e Altura)
Mostre a área do terreno.
'''

def area(l, h):
    a = (l * h)
    print(f'---'* 25)
    print(f'O Retângulo com largura de {l} e altura de {h} tem uma área igual à {a}m²')
    print(f'---'* 25)
    
print(f' Controle de Terrenos ')
print(f'-' * 20)
l = float(input(f'LARGURA (m): '))
c = float(input(f'ALTURA (m): '))
area(l,c)