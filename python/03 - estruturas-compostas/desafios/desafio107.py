'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas: 
    - aumentar(), 
    - diminuir(),
    - dobro(),
    - metade()

faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from modulos import moedas

p = float(input(f'Digite o preço: R$ '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10)}')
print(f'Reduzindo em 13%, temos {moedas.diminuir(p,13)}')