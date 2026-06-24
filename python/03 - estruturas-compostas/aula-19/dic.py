pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()

# Testando apagando elementos
del pessoas ['sexo']

# Testando troca de valores
pessoas ['nome'] = 'Leandro'

# Testando adicionar elementos
pessoas ['peso'] = 98.5

print(f'ITENS: ')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
    
print(f'CHAVES: ')
for k in pessoas.keys():
    print(f'{k}')
print()

print(f'VALORES: ')
for v in pessoas.values():
    print(f'{v}')