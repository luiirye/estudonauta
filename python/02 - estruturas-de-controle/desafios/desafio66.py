'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
Desconsidere o valor 999 (flag)
'''

n = c = s = 0
# Numero, Contador, Soma

while True:
    n = int(input("Digite um número: "))
    
    if n == 999:
        break
    
    c += 1
    s += n

print(f'{c} números foram digitados.\nSoma dos Números = {s}')