# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores "M" ou "F".
# Caso esteja erradp, peça a digitação novamente até ter um valor correto.
'''
# Minha solução
sexo = ''
while sexo != 'M' and 'F':
    
    sexo = str(input("Digite o sexo de uma pessoa [M/F]: ")).upper().strip()

    if sexo != 'M' and 'F':
        print("Escolha apenas uma das duas opções [M/F]")
    elif sexo == 'M':
        print("Sexo selecionado: MASCULINO")
    elif sexo == 'F':
        print("Sexo selecionado: FEMININO")
'''
# Correção professor

sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso!'.format(sexo))