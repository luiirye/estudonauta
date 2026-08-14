a = [2, 3, 4, 7]
b = a[:] # a partir do momento que igualamos uma lista, é criada uma LIGAÇÃO de listas
b[2] = 8
print(f'lista A: {a}')
print(f'Lista B: {b}')