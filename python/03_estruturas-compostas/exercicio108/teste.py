from exercicio108 import moeda

p = float(input(f'Digite um preço: R$'))

print(f'A metade de {moeda.moeda(p)} é  {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é  {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando  {moeda.moeda(p)} em uma taxa de 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo  {moeda.moeda(p)} em uma taxa de 13%, temos {moeda.moeda(moeda.diminuir(p, 10))}')