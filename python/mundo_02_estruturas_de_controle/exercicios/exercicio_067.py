'''
Faça um programa que mostre:
    - A tabuada de vários números, um de cada vez, para cada valor digitado.
    - O programa será interrompido quando o número digitado for negativo
'''
print("==" * 10)
print("TABUADA DE INTEIROS")
print("==" * 10)

while True:
    
    num = int(input("Informe um número para mostrar sua tabuada: "))
    
    if num < 0:
        break
    
    print("===" * 10)
    for c in range(1,11):
        print(f"{num} X {c} = {num*c}")
    print("===" * 10)

print("Programa tabuada encerrado...")