n1 = float(input("Informe a N1: "))
n2 = float(input("Informe a N2: "))

media = (n1 + n2) / 2

print("A sua média é: {:.1f}".format(media))
print('PARABÉNS' if media >= 6.0 else 'ESTUDE MAIS')
if media >= 6.0:
    print("Sua média está boa, parabéns!")
else:
    print("Sua média não está boa, estuda mais!")