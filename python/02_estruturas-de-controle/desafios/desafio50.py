# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquels que forem pares.
# Se for ímpar, desconsidere-o

soma = 0
contador = 0
for i in range (1, 7):
    x = int(input("Informe o {} número: ".format(i)))
    if x % 2 == 0:
        soma += x
        contador += 1
        
print("SOMA = {}".format(soma))
print("NÚMEROS PARES SOMADOS: {}".format(contador))