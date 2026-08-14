#conversor de temperatura

c = float(input("informe a temperatura em °C: "))
conversor_para_f = (((c * 9) / 5) + 32)

print(
    "Temperatura em Celsius: {:.1f} °C.\nTemperatura convertida em Fahrenheit: {:.1f} °F".format(c, conversor_para_f)
)

# Feito