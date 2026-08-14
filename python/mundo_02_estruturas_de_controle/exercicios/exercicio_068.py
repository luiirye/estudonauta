'''
Faça um programa que jogue um par ou ímpar com o computador.
O jogo só será encerreado quando o jogador PERDER.
Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

print("=======" * 4)
print("=== JOGO DE PAR OU ÍMPAR ===")
print("=======" * 4)

vitorias = 0

while True:
    
    print("==" * 10)
    print("Escolha: \n[1] - Par\n[2] - Ímpar")

    opt = int(input(""))
    num = int(input("Informe um número de 0 a 10: "))

    pc = randint(0, 11)
    soma = num + pc

    resultado_par = soma % 2 == 0

    print("==" * 10)
    print(f"Seu número: {num}")
    print(f"Número PC: {pc}")
    print(f"Soma: {soma}")

    if opt == 1 and resultado_par:
        print("É PAR!!")
        print("Você venceu!!")
        vitorias += 1

    elif opt == 2 and not resultado_par:
        print("É ÍMPAR!!")
        print("Você venceu!!")
        vitorias += 1

    else:
        print("Você perdeu...")
        print(f"Vitórias consecutivas: {vitorias}")
        break