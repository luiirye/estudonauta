# Desenvola um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200KM e R$ 0.45 para viagens mais longas

distancia = float(input("Digite a distância da viagem em KM: "))
p1 = 0.50
p2 = 0.45

if distancia <= 200.00:
    print(
        "Distância da viagem: {:.1f} km.\nPreço por km: R$ {:.2f}\nValor da passagem: R$ {:.2f}".format(distancia, p1, (distancia * p1))
    )
else:
    print(
        "Distância da viagem: {:.1f} km.\nPreço por km: R$ {:.2f}\nValor da passagem: R$ {:.2f}".format(distancia, p2, (distancia * p2))
    )