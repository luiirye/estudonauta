# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços

frase = str(input("Digite uma frase: ")).strip().upper() # A string digitada terá seus espaços eliminados, e todas as letras convertidas para maiúsculas.
palavras = frase.split() # Separa a string por palavarsa, colocando dentro de uma lista.
junto = ''.join(palavras) # Junta todas as palavras com o que colocar dentro das ''
print("Você digitou a frase: {}".format(frase))
print("String separadas em palavaras: {}".format(palavras))
print("Tudo junto: {}".format(junto))
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    # o primeiro -1 vai até a última letra
    # o Segundo -1 vai até a primeira letra
    # o terceiro dá um passo negativo
    inverso += junto[letra]

if inverso == junto:
    print('{} {}'.format(junto, inverso))
    print("TEMOS UM PALÍNDROMO!")
else:
    print("A frase digita não é um palíndromo!")