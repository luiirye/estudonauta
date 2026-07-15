'''
Modifique as funções que foram criadas no desafio 107. 
Elas devem aceitar um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

from utilidadesCeV.moedas import moedas

p = float(input(f'Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo em 13%, temos {moedas.diminuir(p, 13, False)}') # Para teste de resultado.