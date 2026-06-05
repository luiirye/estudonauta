'''
Crie umn programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES.
Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.
'''
lista = []
expressao = str(input("Digite um expressão: "))
lista.append(expressao)

for parenteses in expressao:
    print(parenteses)