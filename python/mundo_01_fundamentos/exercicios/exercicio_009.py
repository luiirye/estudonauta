# crie um programa quie leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.

dinheiro = float(input("Informe o quanto de dinheiro tens: R$ "))

dol = 4.92
dol_conversor = dinheiro / dol

print(
    "R$ {:.2f} pode comprar aproximadamente US$ {:.2f}".format(dinheiro, dol_conversor)
)

# Correto
