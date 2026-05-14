# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 - Para binário
# 2 - Para octal
# 3 - para hexadecimal

print("-=-" * 20)
print("Base de conversão")
print("-=-" * 20)

digit = int(input("Digite um número qualquer: "))

print("Escolha uma das opções:\n1 - Converter para BINÁRIO.\n2 - Converter para OCTAL\n3 - Converter para HEXADECIMAL")
opt = int(input(""))

# conversões
binario = bin(digit)
octal = oct(digit)
hexa = hex(digit)

if (opt == 1):
    print("Conversão de {} para binário: {}".format(digit, binario))
elif (opt == 2):
    print("Conversão de {} para Octal: {}".format(digit, octal))
elif (opt == 3):
    print("Conversão de {} para Hexadecimal: {}".format(digit, hexa))
else:
    print("\033[0;31mOpção inválida, programa encerrado...\033[m")