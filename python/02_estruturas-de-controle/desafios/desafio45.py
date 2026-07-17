# Crie um programa que faça o computador jogar jokenpô com você
from random import randint
from time import sleep

## Minha resolução
# print("-=-" * 5)
# print("JOGO DE JOKENPÔ")
# print("-=-" * 5)

# print(
#     "Escolha um dos movimentos abaixo:\n1 - Pedra\n2 - Papel\n3 - Tesoura"
# )

# movimento = int(input())
# rand = randint(1, 3)

# if (movimento == 1 and rand == 1): # Pedra × Pedra
#     print("Você: Pedra\nComputador: Pedra")
#     print("Pedra x Pedra")
#     print("EMPATE!!")
# elif (movimento == 1 and rand == 2): # Pedra × Papel
#     print("Você: Pedra\nComputador: Papel")
#     print("Pedra x Papel")
#     print("VENCEDOR: COMPUTADOR!!")
# elif (movimento == 1 and rand == 3): # Pedra x tesoura
#     print("Você: Pedra\nComputador: Tesoura")
#     print("Pedra x Tesoura")
#     print("VENCEDOR: VOCÊ!!")
# elif (movimento == 2 and rand == 1): # Papel x Pedra
#     print("Você: Papel\nComputador: Pedra")
#     print("Papel x Pedra")
#     print("VENCEDOR: VOCÊ!!")
# elif (movimento == 2 and rand == 2): # Papel x Papel
#     print("Você: Papel\nComputador: Papel")
#     print("Papel x Papel")
#     print("EMPATE!!")
# elif (movimento == 2 and rand == 3): # Papel x Tesoura
#     print("Você: Papel\nComputador: Tesoura")
#     print("Papel x Tesoura")
#     print("VENCEDOR: COMPUTADOR!!")
# elif (movimento == 3 and rand == 1): # Tesoura x Pedra
#     print("Você: Tesoura\nComputador: Pedra")
#     print("Tesoura x Pedra")
#     print("VENCEDOR: COMPUTADOR!!")
# elif (movimento == 3 and rand == 2): # Tesoura x Papel
#     print("Você: Tesoura\nComputador: Papel")
#     print("Tesoura x Papel")
#     print("VENCEDOR: VOCÊ!!")
# elif (movimento == 3 and rand == 3): # Tesoura x Tesoura
#     print("Você: Tesoura\nComputador: Tesoura")
#     print("Tesoura x Tesoura")
#     print("EMPATE!!") # lesbian rsrs
# else:
#     print("Movimento inexistente... Encerramento o programa...")


# Resolução do professor
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print(''' Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA ''')
jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 11)

if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print("EMPATOU")
    elif jogador == 1:
        print("JOGADOR VENCEU")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("Jogada Inválida")

if computador == 1: # Computador jogou Papel
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATOU")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("Jogada Inválida")

if computador == 2: # Computador jogou Tesoura
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATOU")
    else:
        print("Jogada Inválida")