'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na saquência.

No final, mostre uma listagem de preços organizando os dados em forma TABULAR
'''
itens = (
    'Lápis' ,1.75, 
    'Borracha', 2.00, 
    'Caderno', 15.90, 
    'Estojo', 25.00, 
    'Transferidor', 4.20, 
    'Compasso', 9.99, 
    'Mochila', 120.32, 
    'Canetas', 22.30, 
    'Livro', 34.90
)

print("-" * 50)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print("-" * 50)

for item in range(0, len(itens), 2):
    print(f'{itens[item]:.<40}R$ {itens[item + 1]:>7.2f}')
    
print("-" * 50)
