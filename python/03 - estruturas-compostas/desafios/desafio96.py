'''
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular.
dimensões: (largura e Altura)
Mostre a área do terreno.
'''

def area(l, h):
    a = (l * h)
    print(f'---'* 25)
    print(f'O Retângulo com largura de {l} e altura de {h} tem uma área igual à {a}')
    print(f'---'* 25)
    
area(2,3)
area(4,5)
area(10,30)
area(1,2)