'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais Foram os números pares.
'''

n = (
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: ")),
    int(input("Digite um número: "))
)
print(f"Valores digitados: {n}")

# A) Mostra quantas vezes apareceram o número nove
print(f'O valor 9 apareceu {n.count(9)} vezes.')

# B) Mostra em qual posição está inserido o número 3
if 3 in n:
    print(f'O valor 3 apareceu primeiro na {n.index(3)+1}ª posição.')    
else:
    print("O valor 3 não foi digitado em nenhuma posição")

# C) Mostra quais números são pares
print(f'Os valores pares digitados foram: ', end = '')
for numero in n:
    if numero % 2== 0:
        print(numero, end=' ')
