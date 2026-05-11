# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random

nomes = ['Luis Felipe', 'Lara', 'Ruam', 'Ryan']
sorteado = random.choice(nomes)
print("Aluno sorteado: {}".format(sorteado))

