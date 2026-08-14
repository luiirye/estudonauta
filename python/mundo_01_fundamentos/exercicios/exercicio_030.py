# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num =  int(input("Digite um número inteiro qualquer: "))

print(f'O NÚMERO {num} É PAR' if num % 2 == 0 else f'O NÚMERO {num} É ÍMPAR')