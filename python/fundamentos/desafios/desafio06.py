# Desenvolva um programa que leia duas notas d eum aluno, calcule e mostre sua média
nome = input("Informe o nome do aluno: ")
n1 = float(input("Informe a primeira nota desse aluno: "))
n2 = float(input("Informe a segunda nota desse aluno: "))

media = (n1 + n2) / 2 # Média é calculada dividindo pela quantidade de notas

print(
    "Aluno: {}.\nNota 1: {}\nNota 2: {}\nMédia das notas: {:.1f}".format(nome, n1, n2, media)
)

# Correto