'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas: 
    - aumentar(), 
    - diminuir(),
    - dobro(),
    - metade()

faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from utilidadesCeV.moedas import moedas

p = float(input(f'Digite o preço: R$ '))
print(f'A metade de {p} é R$ {moedas.metade(p):.2f}')
print(f'O dobro de {p} é R$ {moedas.dobro(p):.2f}')
print(f'Aumentando 10%, temos R$ {moedas.aumentar(p, 10):.2f}')
print(f'Reduzindo em 13%, temos R$ {moedas.diminuir(p,13):.2f}')