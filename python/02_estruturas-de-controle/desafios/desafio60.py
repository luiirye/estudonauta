# faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5*4*3*2*1 = 120

# Minha resolução
n = int(input("informe um número qualquer inteiro: "))
contador = n
fatorial = 1

print("Calculando {}! = ".format(n), end = '')

while contador > 0:
    
    print('{}'.format(contador), end = '')
    print(' * ' if contador > 1 else ' = ', end = '')
    fatorial *= contador
    contador -= 1
    
print("{}".format(fatorial))



