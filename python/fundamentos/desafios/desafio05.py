# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math # Para importar a função de raiz quadrada

x = float(input("Digite um número qualquer: "))

dobro = (x * 2)
triplo = (x * 3)
# função pow
raiz = (math.sqrt(x))

print(
    "Dobro de {} = {}\nTriplo {} = {}\nRaiz Quadrada de {} = {:.2f}.".format(x, dobro, x , triplo, x, raiz)
)

# Correto