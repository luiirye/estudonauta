'''
Crie umn programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES.
Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.
'''
while True:
    resposta = ''
    
    while resposta in 'Ss':
        
        lista = []
        expressao = str(input("Digite um expressão: "))
        
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
    
        resposta = str(input('Deseja digitar outra expressão? [S/N] ')).upper().strip()[0]
        if resposta == 'N':
            break