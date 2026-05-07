# Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e antecessor

x = int(input("Digite um número inteiro: "))

ant = x - 1
suc = x + 1

print(
    "Número informado: {}\nSucessor de {}: {}\nAntecessor de {}: {}".format(x, x, suc, x, ant)
)