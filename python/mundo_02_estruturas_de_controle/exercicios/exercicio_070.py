'''
Crie um programa que leia o NOME e o PREÇO de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$ 1000,00.
    C) Qual é o nome do produto mais barato.
'''
# variáveis para o exercício
total = 0
totmil = 0
menor = 0
cont =  0
barato = ''

while True:
    
    print("====== COMPRA DE PRODUTOS ======")
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    
    total += preco
    
    if preco > 1000:
        totmil += 1
    
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == 'N':
        break

print("==== TOTAL COMPRA ====")
print(f"Total gasto na compra: R${total:.2f}")
print(f"Quantidade de produtos de menos de R$ 1000,00: {totmil}")
print(f"Produto mais barato foi {barato}, custando: R${menor:.2f}")