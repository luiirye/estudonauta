# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

produto_valor = float(input("Informe o valor do produto: "))

print("Informe a forma de pagamento: ")
print("1 - Á vista ou cheque")
print("2 - Á vista no cartão")
print("3 - Em até 2x no cartão")
print("4 - 3x ou mais no cartão")
opt = int(input())

vista_cheque = produto_valor - (produto_valor * 10/100)
vista_cartao = produto_valor - (produto_valor * 5/100)
cartao = produto_valor + (produto_valor * 20/100)

if (opt == 1):
    print("Forma de pagamento: 1 - Á vista/Cheque.")
    print("Preço Produto: R$ {:.2f}\nNovo preço com 10% de desconto: R$ {:.2f}".format(produto_valor, vista_cheque))
elif (opt == 2):
    print("Forma de pagamento: 2 - Á vista no cartão")
    print("Preço Produto: R$ {:.2f}\nNovo preço com 5% de desconto: R$ {:.2f}".format(produto_valor, vista_cartao))
elif (opt == 3):
    print("Forma de pagamento: 3 - Em até 2x no cartão")
    print("Preço normal à pagar.\nPreço produto: R$ {:.2f}".format(produto_valor))
elif (opt == 4):
    print("Forma de pagemento: 4 - 3x ou mais no cartão")
    print("Preço produto: R$ {:.2f}\nNovo preço com 20% de juros: R$ {:.2f}".format(produto_valor, cartao))
else:
    print("Selecione alguma das opções acima. reinicie o programa.")