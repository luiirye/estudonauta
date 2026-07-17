# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida:
# O primeiro e o último nome separadamente.
# Exemplo: Ana maria de Souza
# primeiro: Ana
# ùltimo: Souza

nome = str(input("informe o nome completo de uma pessoa: ")).strip() # Adicionado strip

n = nome.split() # Adicionado variável "n" para melhor entendimento nos Prints

print("=" * 100)
print(
    "Nome Completo informado: {}".format(nome)
)
# 1
print(
    "Prmeiro nome: {}".format(n[0])
)
# 2
print(
    "Último nome: {}".format(n[len(n) - 1]) # Adicionado Len - 1 para pegar a última posição.
)