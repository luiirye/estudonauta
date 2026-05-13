# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo  número: "))
n3 = float(input("Informe o terceiro número: "))

if (n1 > n2 > n3):
    print("{} é menor".format(n3))
elif (n1 > n2 < n3):
    print("{} é menor".format(n2))
elif (n1 < n2 > n3):
    print("{} é menor".format(n1))
elif (n1 < n2 < n3):
    print("{} é menor".format(n1))
elif (n1 == n2 == n3):
    print("Números iguais.")