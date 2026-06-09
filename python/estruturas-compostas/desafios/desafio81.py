'''
Crie um programa que vai ler vários números e colocar em uma lista.

depois disso, mostre:
A) QUANTOS números foram digitados.
B) A lista de valores ordenada de forma DECRESCENTE
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = [] # Lista de números iniciando vazia
cont = cinco = 0

while True:
    num = int(input("Digite um número para incluir na lista: "))
    numeros.append(num) # Adicionando o número á lista
    cont += 1 # Contador para dizer quantos números foram digitados

    resposta = str(input(f'Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
    
numeros.reverse()
cinco = numeros.count(5)

print(f'-=' * 15)
print(f"Fim da Lista! Foram digitados {cont} números ao total.")
print(f'Lista na ordem decrescente: {numeros}')

if cinco > 0:
    print(f"O valor 5 foi digitado {cinco} vezes.")
else:
    print(f"O valor 5 não foi digitado nenhuma vez")

print(f'-=' * 15)