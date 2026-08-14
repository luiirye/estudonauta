'''
Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
'''
numeros  = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
    'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
    'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

while True:

    n = int(input("Digite um número de 0 até 20: "))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end = '')

print(f"numero informado: {n}\n{n} escrito por extenso: {numeros[n]}")