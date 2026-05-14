# Escreva um programa que leia dois números inteiros e os compare, mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print("-=-" * 10)
print("\033[4;36;47m COMPARAÇÃO ENTRE DOIS NÚMEROS \033[m")
print("-=-" * 10)

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número : "))

if (n1 > n2):
    print("O primeiro valor é maior")
elif (n1 < n2):
    print("O segundo valor é maior")
elif (n1 == n2):
    print("Não existe valor maior, os dois valores são iguais")
