# Crie um programa que leia un nome completo de uma pessoa e mostre:
# 1 - o nome com todas as letras maiúsculas
# 2 - o nome com todas as letras minúsculas
# 3 - Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input("Insira seu nome completo: ")).strip()

print("="*100)
print(
    "Nome/String informada: {}".format(nome)
)
# 1
print(
    "Nome com todas as letras maísuculas: {}".format(nome.upper())
)

# 2
print(
    "Nome com todas as letras minúsculas: {}".format(nome.lower())
)

# 3
print(
    "Quantidade de letras ao todo(sem espaços): {}".format(len(nome.replace(" ", "")))
)

# 4
separa = nome.split()[0] # -> Separa em uma lista todas as palavras do nome e pega o da primeira posição ['Luis', 'Felipe', 'Borges'] -> [0,1,2]
print(
    "Quantidade de letras do primeiro nome: {}".format(len(separa))
)
print("="*100)
