'''
Crie um programa que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = [] # lista vazia para números

while True:
    num = (int(input("Digite um número: ")))
    numeros.append(num)
    
    if numeros.count(num) > 1:
        print(f"Número {num} já existente na lista. Não será adicionado")
        numeros.pop() # Para remover o último elemento adicionado
        break

numeros.sort()

print(
    f'Fim da lista.\nLista de todos os números digitados ordenados:\n{numeros}'
)