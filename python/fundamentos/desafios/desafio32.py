# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input("Informe um ano qualquer: "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("{} é bissexto".format(ano))
else:
    print("{} não é bissexto".format(ano))