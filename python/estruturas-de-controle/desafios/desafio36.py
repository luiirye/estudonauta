# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print("-=-"*30)
print("APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA")
print("-=-"*30)

valor_casa = float(input("Informe o valor da casa: "))
salario_comprador = float(input("Informe o salário do comprador: "))
anos = float(input("Em quantos anos pretende pagar? "))
calculo_prestacao = valor_casa / (anos * 12) 

if (calculo_prestacao <= (salario_comprador  * 30/100)):
    print("Empréstimo de R$ {:.2f} aprovado!!".format(calculo_prestacao))
elif (calculo_prestacao > (salario_comprador * 30/100)):
    print("Empréstimo negado!\nPrestação maior que 30% do salário.")
elif (calculo_prestacao == salario_comprador):
    print("Empréstimo Nefado!\nPrestação igual ao salário informado.")