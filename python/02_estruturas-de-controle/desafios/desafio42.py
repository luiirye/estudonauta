# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Pode formar um triângulo")
    if (a == b == c): # Correto
        print("Formam um triângulo EQUILÁTERO.")
    elif (a == b or b == c): 
        print("Formam um triângulo ISÓCELES.")
    elif (a != b and b != c):
        print("Formam um triângulo ESCALENO")
else:
    print("Não pode formar um triângulo")