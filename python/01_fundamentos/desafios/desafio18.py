# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, e a tangente desse ângulo

from math import cos, sin, tan, radians

x = float(input("Digite um ângulo qualquer: "))
convertx = radians(x)
cx = cos(convertx)# cosseno de x
sx = sin(convertx)# seno de x
tx = tan(convertx)# tangente de x


print(
    "Ângulo: {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(x, sx, cx, tx)
)
