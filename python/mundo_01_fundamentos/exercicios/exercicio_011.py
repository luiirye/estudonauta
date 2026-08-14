# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco_prod = float(input("Informe o preço do produto: "))
off = preco_prod * 5/100
novo_preco = preco_prod - off

print(
    "Preço do produto: R$ {:.2f}\nDesconto de 5%: R$ {:.2f}\nPreço com 5% aplicado: R$ {:.2f}".format(preco_prod, off, novo_preco)
)

#Correto
