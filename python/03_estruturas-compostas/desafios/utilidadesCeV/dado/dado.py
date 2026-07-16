def leiaDinheiro():
    
    while True:
        
        numero = str(input(f'teste: ')).isnumeric()

        if numero == True:
            print(F'Número lido e validado com sucesso')
            break
        else:
            print(f'Digite um valor válido...')

leiaDinheiro()