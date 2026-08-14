'''
Faça um programa que tenha uma função chamada escreva().
A função deve receber um texto qualquer como PARÂMETRO e mostre uma mensagem com tamanho adaptável.

Ex: excreva('Olá, Mundo!')
Saída:
------------------- -> tem que adaptar as linhas
    Olá, Mundo!    
-------------------      
'''

def escreva(texto):
    mensagem = f'    {texto}    '
    
    for i in range(len(mensagem)):
        print(f'-', end='')
    print()
    
    print(mensagem)
    
    for i in range(len(mensagem)):
        print(f'-', end='')
    print()
    

print(f'Mensagem adaptável:')
print(f'-' * 20)
mensagem = str(input(f'Digite uma mensagem qualquer: '))

escreva(mensagem)