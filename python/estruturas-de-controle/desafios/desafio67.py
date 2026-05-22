'''
Faça um programa que mostre:
    - A tabuada de vários números, um de cada vez, para cada valor digitado.
    - O programa será interrompido quando o número digitado for negativo
'''
print("==" * 10)
print("TABUADA DE INTEIROS")
print("==" * 10)

n = t = 0
mult = 1
while True:
    
    n = int(input("Digite um número para mostrar sua tabuada: "))
    t = n * mult
    
    if mult <= 10:
        print(
            f'{n} * {mult} = {t}'
        )
    
    mult += 1
    
    if mult == 10:
        mult == 1
    
    if n < 0:
        print("Programa encerrado...")
        break
