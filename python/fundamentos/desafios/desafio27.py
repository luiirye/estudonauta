# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida:
# O primeiro e o último nome separadamente.
# Exemplo: Ana maria de Souza
# primeiro: Ana
# ùltimo: Souza

nome = str(input("informe o nome completo de uma pessoa: "))
print("=" * 100)
print(
    "Nome Completo informado: {}".format(nome)
)
# 1
print(
    "Prmeiro nome: {}".format(nome.split()[0])
)
# 2
print(
    "Último nome: {}".format(nome.split())
)