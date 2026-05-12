tempo1 = int(input("Quantos anos tem seu carro?"))

if (tempo1 <= 3):
    print("Carro novo")
else:
    print("Carro velho")

print("--FIM--")

## OU

tempo2 = int(input("Quantos anos tem seu carro?"))
print('carro novo'if tempo2 <= 3 else 'carro velho')
print('--FIM--')