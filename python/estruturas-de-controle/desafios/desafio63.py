# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os "n" primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

from math import sqrt

# tentando separar os problemas em pequenas partes
# primeira parte: ler um número N
n = int(input("Informe um número inteiro qualquer: "))

# sequência de fibonacci
# informação: cada termo é a soma dos dois termos anteriores

a1 = 1
a2 = 1
fibonacci = 0
count = 1

while fibonacci <= n:
    
    if n == 1 or n == 2:
        print("1")
        fibonacci = n + 1
        
    else:
        fibonacci = a1 + a2
        print("termo: {} -> {} + {} = {}".format(count, a1, a2, fibonacci))
        a1 = a2
        a2 = fibonacci
        count += 1 # contador para saber qual termo é qual
    

print("fim do programa")