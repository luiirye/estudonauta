# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os "n" primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

from math import sqrt

# tentando separar os problemas em pequenas partes
# primeira parte: ler um número N
print("--" * 15)
print("Sequência de Fibonacci")
print("--" * 15)

n = int(input("Quantos termos você quer mostrar? "))

# sequência de fibonacci
a1 = 0
a2 = 1
print("~" * 30)
print("{} -> {}".format(a1, a2), end = '')
contador = 3
while contador <= n:
    a3 = a1 + a2
    print(" -> {}".format(a3), end = '')
    a1 = a2
    a2 = a3
    contador += 1
print("-> FIM")
