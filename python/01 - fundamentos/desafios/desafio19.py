# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
from random import choice

n1 = str(input("Primeiro Aluno: "))
n2 = str(input("Segundo Aluno: "))
n3 = str(input("Terceiro Aluno: "))
n4 = str(input("Quarto Aluno: "))
lista = [n1, n2 , n3, n4]
sorteado = choice(lista) # Função da biblioteca random para escolher aleatóriamente um dos itens da lista
print("Aluno escolhido/sorteado: {}".format(sorteado))

