# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Informe seu salário: "))
aumento = salario + (salario * 15/100)

print(
    "Salário informado: R$ {:.2f}\nSalário com 15% de aumento: R$ {:.2f}".format(salario, aumento)
) 