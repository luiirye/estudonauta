from exercicio107 import moeda

p = float(input(f'Digite um preço: R$'))

print(f'A metade de R$ {p:.2f} é R$ {moeda.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moeda.dobro(p):.2f}')
print(f'Aumentando R$ {p:.2f} em uma taxa de 10%, temos R$ {moeda.aumentar(p, 10):.2f}')
print(f'Diminuindo R$ {p:.2f} em uma taxa de 13%, temos R$ {moeda.diminuir(p, 10):.2f}')