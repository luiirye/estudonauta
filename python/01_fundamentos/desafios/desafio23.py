## Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# exemplo: 1834
# Unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = str(input("Insira um número de 0 a 9999: "))
print("=" * 100)
# print(numero)
# print(
#     "Utilizando posições de Strings\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n".format(numero[3], numero[2], numero[1], numero[0])
# )
# print("=" * 100)

# divide o valor pelo casa de unidade (divisão inteira) e atribui o resto á variáveil, fazendo a mesma coisa para as demais 

int_numero = int(numero)
mil = int_numero // 1000
int_numero %= 1000
cent = int_numero // 100
int_numero %= 100
dez = int_numero // 10
int_numero %= 10
uni = int_numero // 1

print(int(numero))  # convertendo para inteiro

print(
    "Forma matemática de realizar:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(uni, dez, cent, mil)
)