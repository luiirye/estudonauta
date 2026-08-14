# Escreva um programa que leia um valor em metros e o exiba convertido em CENTÍMETROS a MILÍMETROS

x = float(input("Informe o valor em metros: "))

km = 1000
hm = 100
dam = 10
dm = 10
cm = 100
mm = 1000

calculo_km = x / km
calculo_hm = x / hm
calculo_dam = x / dam
calculo_dm = x * dm
calculo_cm = x * cm
calculo_mm = x * mm

print(
    "Conversor de {:.2f} metros:\n{:.2f} km\n{:.2f} hm\n{:.2f} dam\n{:.2f} dm\n{:.2f} cm\n{:.2f} mm".format(x,calculo_km, calculo_hm, calculo_dam ,calculo_dm, calculo_cm, calculo_mm)
)

# Correto