# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os infeiores ou iguais, o aumento é de 15%

salario = float(input("Informe o salário: "))

if (salario  <= 1250.00):
    calculo = (salario * 15/100) + salario
    print(
        "Salário inicial: R$ {:.2f}\nSalário com aumento de 15%: R$ {:.2f}".format(salario, calculo)
    )
else:
    calculo = (salario * 10/100) + salario
    print(
        "Salário inicial: R$ {:.2f}\nSalário com aumento de 10%: R$ {:.2f}".format(salario, calculo)
    )