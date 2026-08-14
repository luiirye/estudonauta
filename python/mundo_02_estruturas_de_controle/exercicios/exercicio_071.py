'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$1,00, R$10,00, R$20,00 e R$50,00
'''

print("=" * 30)
print('{:^30}'.format('BANCO CEV'))
print("=" * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print("=" * 30)
print('Volte sempre ao BANCO CEV. Tenha um bom dia!')
print("=" * 30)