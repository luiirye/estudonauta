# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²


l = float(input("Informe a largura: "))
h = float(input("Informe a altura: "))

area = h * l
litro_tinta = 2
qntd_tinta = area / litro_tinta

print(
    "largura: {}\naltura: {}\narea: {} m²\nTinta por metro²: {}\nQuantidade de tinta necessário: {} Litros".format(l, h, area, litro_tinta, qntd_tinta)
)

# Correto
