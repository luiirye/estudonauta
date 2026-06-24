from math import trunc

# Crie um programa que leia um número real qualquer pelo teclado e mostra na tela a sua porção inteira

x = float(input("Digite um número real qualquer: "))

truncado = trunc(x)

print(
    "Número informado: {}\nParte inteira: {}".format(x, truncado)
)