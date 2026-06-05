'''
Crie um programa que vai ler vários números e colocar em uma lista.

depois disso, mostre:
A) QUANTOS números foram digitados.
B) A lista de valores ordenada de forma DECRESCENTE
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = [] # Lista de números iniciando vazia
cont = tamanho = cinco = 0

while True:
    num = int(input("Digite um número para incluir na lista: "))
    numeros.append(num) # Adicionando o número á lista
    cont += 1 # Contador para dizer quantos números foram digitados
    
    resposta = str(input("Quer digitar outro número? [S/N] ")).upper()[0].strip()
    
    while resposta not in 'SN':
        resposta = str(input("Quer digitar outro número? [S/N] ")).upper()[0].strip()
    if resposta == 'N':
        break

numeros.sort()
numeros.reverse()
tamanho = len(numeros)
cinco = numeros.count(5)

print(f'-=' * 15)
print(f"Fim da Lista! Foram digitados {cont} números ao total.")
print(f'Lista na ordem decrescente: {numeros}')

if cinco > 1:
    print(f"O valor 5 foi digitado {cinco} vezes.")
else:
    print(f"O valor 5 não foi digitado nenhuma vez")

print(f'-=' * 15)