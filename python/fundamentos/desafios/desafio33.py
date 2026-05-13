# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo  número: "))
n3 = float(input("Informe o terceiro número: "))

if (n1 < n2 and n2 < n3):
    print("{} é menor\n{} é maior".format(n1,n3))
elif (n1 < n3 and n2 > n3):
    print("{} é menor\n{} é maior".format(n1,n2))
elif (n1 > n2 and n2 > n3):
    print("{} é menor\n{} é maior".format(n3,n1))
elif (n1 > n3 and n2 < n3):
    print("{} é menor\n{} é maior".format(n2,n1))
elif (n1 == n2 and n2 == n3):
    print("Números iguais.")