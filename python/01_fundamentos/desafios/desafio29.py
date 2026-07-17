# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite

vel = float(input("Informe a velocidade do carro: "))
if vel > 80.00:
    print(
        "Você ultrapassou {:.1f}km do permitido ({:.1f} km). Multa aplicada!\nTotal multa: R$ {:.2f}".format((vel  - 80),80.00,(vel - 80.00) * 7.00)
    )
else:
    print(
        "Velocidade dentro do limite."
    )