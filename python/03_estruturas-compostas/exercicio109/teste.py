from moeda import dobro , metade, moeda, aumentar, diminuir

p = float(input(f'Digite um preço: R$'))

print(f'A metade de {moeda(p)} é  {metade(p, True)}')
print(f'O dobro de {moeda(p)} é  {dobro(p, True)}')
print(f'Aumentando  {moeda(p)} em uma taxa de 10%, temos {aumentar(p, 10, True)}')
print(f'Diminuindo  {moeda(p)} em uma taxa de 13%, temos {diminuir(p, 13, True)}')