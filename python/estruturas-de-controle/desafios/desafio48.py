# Crie um programa que calcule a soma entre todos os NÚMEROS ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 a 1500
soma = 0

for x in range(1, 1501, 3):
        if x % 2 != 0:
            soma += x

print("A SOMA DE TODOS OS ÍMPARES É: {}".format(soma))