galera = list()
dado = list()
totmaior = totmenor = 0
for contador in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
    
    
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade de idade')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} de idade')