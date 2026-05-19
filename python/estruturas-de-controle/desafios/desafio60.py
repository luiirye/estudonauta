# faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5*4*3*2*1 = 120

fatorial = 0

while fatorial != 1:
    
    n = int(input("informe um número qualquer inteiro: "))
    
    fatorial *= n - 1
    
print("{}! = {}".format(n, fatorial))