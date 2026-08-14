# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print("-=-"*30)
print("APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA")
print("-=-"*30)

valor_casa = float(input("Informe o valor da casa: R$ "))
salario_comprador = float(input("Informe o salário do comprador: R$ "))
anos = float(input("Em quantos anos pretende pagar? "))
calculo_prestacao = valor_casa / (anos * 12)
minimo = salario_comprador * (30/100)

print("Para pagar uma casa de R$ {:.2f} em {:.0f} anos,".format(valor_casa, anos), end=' ')
print("a prestação será de R$ {:.2f}".format(calculo_prestacao))

if (calculo_prestacao <= minimo):
    print("Empréstimo de R$ {:.2f} Aprovado!!".format(calculo_prestacao))
elif (calculo_prestacao > minimo):
    print("Empréstimo Negado!\nPrestação maior que 30% do salário.")
elif (calculo_prestacao == salario_comprador):
    print("Empréstimo Negado!\nPrestação igual ao salário informado.")