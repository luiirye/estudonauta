# Aluguel de carros

# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$ 0,15 por KM rodado

aluguel = 60.00
prec_por_km = 0.15

dias = int(input("Por quantos dias o carro foi alugado?: "))
km_rodados = float(input("Qauntos Km rodados?: "))

valor_dias = (dias * aluguel)
valor_km = (prec_por_km * km_rodados)
total = valor_dias + valor_km

print("=" * 40)
print("Valor do aluguel: R$ {}".format(aluguel))
print("Preço por KM rodado: R$ {}".format(prec_por_km))
print("Quantidade de dias alugado: {} dias".format(dias))
print("Km rodados: {} km".format(km_rodados))
print("Valor do aluguel: R$ {:.2f}".format(valor_dias))
print("Valor de Km Rodados: R$ {:.2f}".format(valor_km))
print("Total a pagar: R$ {:.2f}".format(total))
print("=" * 40)