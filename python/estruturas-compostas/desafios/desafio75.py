'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais Foram os números pares.
'''
cont9 = 0
pos3 = 0

n1 = int(input("Insira um valor: "))
n2 = int(input("Insira um valor: "))
n3 = int(input("Insira um valor: "))
n4 = int(input("Insira um valor: "))

tupla = (n1, n2, n3 , n4)

# A) Mostra quantas vezes apareceram o número nove
for cont in range (0, len(tupla)):
    if tupla[cont] == 9:
        cont9 += 1

if cont9 == 0:
    print("Nenhum valor 9 inserido na tupla.")
else:
    print(f"O valor 9 apareceu {cont9} vezes.")

# B) Mostra em qual posição está inserido o número 3
    
for pos in range(len(tupla)):
    if tupla[pos] == 3:
        pos3 = pos

if pos3 < 0:
    print("Nenhum valor 3 inserido na tupla.")
else:
    print(f"O valor 3 está na posição {pos3}")
    
# C) Mostra quais números são pares

for numero in range(0, len(tupla)):
    if tupla[numero] % 2 == 0:
        print(f"{tupla[numero]} é par")