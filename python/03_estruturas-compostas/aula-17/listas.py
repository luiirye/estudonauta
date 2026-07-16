valores = [] # lista vazia
for cont in range(0, 5):
    valores.append(int(input('Digite um valor inteiro: ')))

for chave, valor in enumerate(valores):
    print(f'na posição {chave} encontrei o valor {valor}!')
print("Cheguei ao final da lista.")