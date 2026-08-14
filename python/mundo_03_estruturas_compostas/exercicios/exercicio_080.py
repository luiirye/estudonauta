'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção(sem usar o sort()).

No final, mostre a listsa ordenada na tela.
'''

lista = list() #Lista vazia


for contador in range(0,5):
    n = int(input('Digite um valor: '))
    
    if contador == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da Lista...')
    else: 
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado à posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
            
            