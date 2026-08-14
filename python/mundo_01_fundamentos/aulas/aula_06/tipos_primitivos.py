class TiposPrimitivos:
    
    n1 = int(input('Digite um número:')) # Solicita ao usuário que digite algo e armazena na variável n1
    n2 = float(input('Digite outro número:')) # Solicita ao usuário que digite algo e armazena na variável n2
    n3 = bool(input('Digite um valor booleano (True/False):')) # Solicita ao usuário que digite algo e armazena na variável n3
    n4 = str(input('Digite uma string:')) # Solicita ao usuário que dig
    
    s = n1 + n2 # Soma os números n1 e n2, resultando em uma nova string que é a junção de ambas
    print(f'A soma de {n1} + {n2} é = {s}') # Imprime a mensagem com os valores de n1, n2 e a concatenação s
    
    # Tipos primitivos
    # int, float, bool, str
    
    print(type(n1)) # Imprime o tipo da variável n1, que é int
    print(type(n2)) # Imprime o tipo da variável n2, que é float
    print(type(n3)) # Imprime o tipo da variável n3, que é bool
    print(type(n4)) # Imprime o tipo da variável n4, que é str