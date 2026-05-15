# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artíficio
# Indo de 10 até 0, com uma pausa de 1 segundo entre elas
from time import sleep

for x in range(10, 0, -1):
    print(x)
    sleep(1)

print("POW")
print("Fogos de artíficio")