'''
Crie umn programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES.
Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.
'''
lista = list() # Lista vazia
exp = str(input(f'Digite uma expressão para analisá-la: '))
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')