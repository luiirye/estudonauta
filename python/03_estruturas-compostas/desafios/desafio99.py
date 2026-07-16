'''
faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

Flush no print
'''
def linha():
    print(f'-=' * 30)

def maior(* valores):
    
    maior = menor = 0
    numeros = list()
    
    if len(valores) == 1:
        
        menor = valores
        maior = valores
        
        print(f'Números informados: {len(valores)}')
        print(f'Menor valor é {menor} e o maior também é {maior}. Apenas um valor.')
        
    elif len(valores) > 1:
        
        for num in valores:
            numeros.append(num)
        
        menor = min(valores)
        maior = max(valores)
        
        print(f'Números informados: ', end = '')
        for i in valores:
            print(f'{i}', end = ' ')
        print()
        print(f'O maior valor é {maior} e o menor é {menor}')
        
    elif len(valores) == 0:
        
        print(f'Números informados: {len(valores)}')
        print(f'Nenhum valor informado')

# Teste 1
linha()
maior(1)

# Teste 2
linha()
maior(1,2,3,4,5)

# Teste 3
linha()
maior(45,23)

# Teste 4
linha()
maior()

# Teste 5
linha()
maior(1,2,4,5,6,7,8,0,11,99,777,999,-1)