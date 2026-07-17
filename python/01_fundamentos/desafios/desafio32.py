# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date

ano = int(input("Informe um ano qualquer para analisar. Ou digite 0 para analisar o ano atual. "))

if ano == 0:
    ano = date.today().year

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("{} é bissexto".format(ano))
else:
    print("{} não é bissexto".format(ano))