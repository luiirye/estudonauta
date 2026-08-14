# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input("Digite um número: "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = '') # se for divísivel por 1 e ele mesmo
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divísivel {} vezes'.format(num, tot))

if tot == 2:
    print("É PRIMO!!")
else:
    print("NÃO É PRIMO")