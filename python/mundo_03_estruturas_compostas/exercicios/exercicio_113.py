'''
Reescreva a função leiaInt() que fizemos no desafio 104.
Incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat(f'Digite um valor Real: ')
print(f'O valor inteiro foi {n1} e o número real foi {n2}')