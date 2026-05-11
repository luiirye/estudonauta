# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite o nome de alguma pessoa: "))
print("=" * 50)
print(
    "Nome: {}".format(nome)
)
print(
    "Tem 'SILVA'?\n{}".format('SILVA' in nome.upper())
)
print("=" * 50)