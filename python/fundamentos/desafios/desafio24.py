# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não o nome "SANTO"

cidade = str(input("Digite o nome de alguma cidade: "))
print("=" * 100)
print(
    "Nome da cidade: {}".format(cidade)
)
print(
    "Começa com 'SANTO'? {}".format('SANTO' in cidade.split()[0].upper())
    # Verifica se tem a palavra "SANTO" na cidade, transformando toda a string e maiúscula para a verificação
)