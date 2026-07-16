'''
Crie um programa que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = list() # lista vazia para números

while True:
    n = int(input('Digite um valor: '))
    
    if n not in numeros:
        numeros.append(n)
        print(f'Valor adicionado com sucesso!')
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    
    resposta = str(input('Quer Continuar? [S/N] '))
    
    if resposta in 'Nn':
        break

numeros.sort()
print(f'-=' * 30)
print(f'Você digitou os valores: {numeros}')