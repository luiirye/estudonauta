# Crie um programa que calcule a soma entre todos os NÚMEROS ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 a 500
soma = 0 # Acumulador
contador = 0

for x in range(1, 501, 2):
        if x % 3 == 0:
            soma += x
            contador += 1

print("A SOMA DE TODOS OS ÍMPARES É: {}".format(soma))
print("Quantidade de números: {}".format(contador))
