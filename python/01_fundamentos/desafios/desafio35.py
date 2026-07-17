# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")