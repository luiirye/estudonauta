'''
Crie umn programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES.
Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.
'''
lista = []
expressao = str(input("Digite uma expressão: "))
        
print(f'Expressão digitada: {expressao}')

for i in expressao:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if not lista: # verifica se a lista está vazia
            print('Expressão Inválida')
        else:
            lista.pop()
            if not lista:
                print('Expressão Válida')