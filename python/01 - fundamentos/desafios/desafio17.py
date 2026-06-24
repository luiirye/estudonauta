# Faça um programa que leia o comprimento do cateto oposto e a do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da Hipotenusa
from math import sqrt, pow, hypot

print("=" * 50)
print("Importando as funcionalidades pow e sqrt (potência e raiz quadrada)")
b = float(input("informe o cateto adjacente: "))
c = float(input("informe o cateto oposto: "))

qb = pow(b, 2) 
qc = pow(c, 2)
a = sqrt(qb + qc)

print(
    "Cateto Adjacente: {:.2f}²\nCateto Oposto: {:.2f}²\nSoma dos catetos: {:.2f}² = {:.2f} + {:.2f}² = {:.2f} == {:.2f}\nHipotenuza: Raiz de {:.2f} = {:.4f}".format(b, c, b, qb, c, qc, (qb + qc),(qb + qc), a)
)

## Forma matemática de se resolver hipotenuza sem as funções
print("=" * 50)
print("Forma matemática de resolução")
hi = (b ** 2 + c ** 2) ** (1/2)
print(
    "Cateto Adjacente: {:.2f}²\nCateto Oposto: {:.2f}²\nSoma dos catetos: {:.2f}² = {:.2f} + {:.2f}² = {:.2f} == {:.2f}\nHipotenuza: Raiz de {:.2f} = {:.4f}".format(b, c, b, qb, c, qc, (qb + qc),(qb + qc), hi)
)
print("=" * 50)

print("Importando a função hypot")
hy = hypot(b, c)
print(
    "Cateto Adjacente: {:.2f}²\nCateto Oposto: {:.2f}²\nSoma dos catetos: {:.2f}² = {:.2f} + {:.2f}² = {:.2f} == {:.2f}\nHipotenuza: Raiz de {:.2f} = {:.4f}".format(b, c, b, qb, c, qc, (qb + qc),(qb + qc), hy)
)

