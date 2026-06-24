def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1 # aumenta uma posição
    
valores = list([1,2,3,4,5,6,7,8])
print(valores)
dobra(valores)
print(valores)