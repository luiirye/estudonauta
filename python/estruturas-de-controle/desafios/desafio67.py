'''
Faça um programa que mostre:
    - A tabuada de vários números, um de cada vez, para cada valor digitado.
    - O programa será interrompido quando o número digitado for negativo
'''
print("==" * 10)
print("TABUADA DE INTEIROS")
print("==" * 10)

num = int(input("Informe um número para mostrar sua tabuada: "))
m = 1 

while True:
    
    total = num * m
    print(f"{num} * {m} = {total}")
    m += 1
    
    if m == 11:
        m = 1
        num = int(input("Digite outro número: "))
        if num < 0:
            print("Encerrando tabuada...")
            break