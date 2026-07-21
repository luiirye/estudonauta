'''
Reescreva a função leiaInt() que fizemos no desafio 104.
Incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor


def leiaFloat(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num:
            valor = float(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor

# Programa Principal
n1 = leiaInt(f'Digite um número inteiro: ')
n2 = leiaFloat(f'Digite um número real: ')
print(f'Você digitou o número inteiro {n1}\nE o número real: {n2}')