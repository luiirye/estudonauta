# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra: "A"
# 2 - Em que posição ela aparece pela primeira vez
# 3 - Em que posição ela aparece pela última vez

frase = str(input("Digite uma frase qualquer: "))
print("=" * 100)
print(
    "Frase: {}".format(frase)
)
# 1
print(
    "Quantas letras 'A' aparecem na frase: {}".format(frase.count('A'))
)
# 2
print(
    "Posição em que 'A' aparece pela PRIMEIRA vez: {}".format(frase.find('A')) # Exibe a posição da primeira letra A da frase
)
# 3
print(
    "Posição em que 'A' aparece pela ÚLTIMA vez: {}".format(frase.count)
)
print("=" * 100)