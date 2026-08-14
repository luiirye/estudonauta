lanche = ('hamburguer','Suco','pizza','Pudim', 'Bata Frita')

print(lanche[2])
print(lanche[0:2])
print(lanche[-2])

print('\n')

print(len(lanche)) # tamanho da tupla

print('\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('\n')

for pos, comida in enumerate(lanche): # cria uma variável simples "comida" e acessa índice por índice da tupla, lista, etc
    print(f'Eu vou comer {comida} na posição {pos}')
print(f'Comi pra caramba')
    
# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'Refrigerante'