'''
Crie um programa onde o usuário possa digitar sete valores numéricos.
Cadastre-os em uma LISTA ÚNICA que mantenha separado os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem CRESCENTE
'''
lista = list([[] , []]) # Declara uma lista com duas listas dentro.

for i in range(0, 7):
    
    num = int(input(f'Digite o {i + 1}° número: '))    
    
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
    
# Ordenação
lista[0].sort()
lista[1].sort()

print(f'-=' * 30)
print(f'Lista de pares: {lista[0]}')
print(f'Lista de ímpares: {lista[1]}')
print(f'-=' * 30)