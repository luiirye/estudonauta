# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquels que forem pares.
# Se for ímpar, desconsidere-o

soma = 0
for i in range (0, 6):
    x = int(input("Informe um número: "))
    if x % 2 == 0:
        soma += x
        
print("SOMA = {}".format(soma))