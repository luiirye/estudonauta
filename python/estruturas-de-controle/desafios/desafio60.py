# faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5*4*3*2*1 = 120
print("=== ===")
fatorial = 1

n = int(input("informe um número qualquer inteiro: "))
nex = n

while n > 1:
    
    fatorial = fatorial * n
    n -= 1
    
print("{}! = {}".format(nex, fatorial))