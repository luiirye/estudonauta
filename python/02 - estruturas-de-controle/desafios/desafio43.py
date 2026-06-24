# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 a 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input("Informe o peso: "))
h = float(input("Informe a altura (em metros): "))
IMC = (peso / (h ** 2))

if (IMC < 18.5):
    print("IMC: {:.1f}.\nABAIXO DO PESO.".format(IMC))
elif (IMC > 18.5 and IMC <= 25.0):
    print("IMC: {:.1f}.\nPESO IDEAL".format(IMC))
elif ((IMC > 25.0 and IMC <= 30.0)):
    print("IMC: {:.1f}.\nSOBREPESO".format(IMC))
elif (IMC > 30.0 and IMC <= 40.0):
    print("IMC: {:.1f}.\nOBESIDADE".format(IMC))
else:
    print("IMC: {:.1f}.\nOBESIDADE MÓRBIDA".format(IMC))