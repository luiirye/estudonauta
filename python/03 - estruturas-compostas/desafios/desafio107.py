'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas: 
    - aumentar(), 
    - diminuir(),
    - dobro(),
    - metade()

faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from desafio107 import moeda

p = float(input(f'Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.metade(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(p,13)}')