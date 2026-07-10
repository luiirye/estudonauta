'''
Crie um programa que tenha uma função leiaInt()
ela vai funcionar de forma semelhante à função input(), só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um número')
'''
def leiaint(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor

# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
