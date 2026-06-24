ficha = list()

while True:
    
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    ficha.append([nome, [nota1, nota2], media])
    
    resposta = str(input(f'Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    print('-' * 35)
    opt = int(input("Mostrar notas de qual aluno? (999 Para): "))
    if opt == 999:
        print(f'FINALIZANDO...')
        break
    if opt <= len(ficha) - 1:
        print(f'Notas de {ficha[opt][0]} são {ficha[opt][1]}')
print(f'<<< VOLTE SEMRPE >>>')