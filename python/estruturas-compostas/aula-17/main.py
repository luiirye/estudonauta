# tupla
num = (2,5,9,1)
#lista
n = [2, 5, 9, 1]
n[2] = 3
n.append(7) # adiciona o valor 7 no final
print(n)
n.sort()
print(f"sort {n}")
n.reverse()
print(f'reverse: {n}')
n.insert(2, 2) # adiciona zero na posição 2
print(f'inser: {n}')
n.pop() # remove o último elemento
if 4 in n:
    n.remove(4)
else:
    print(f'Não achei o número 4')
print(f'Elimina o último valor: {n}')