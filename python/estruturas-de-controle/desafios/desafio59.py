# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

# Leitura dos dois valores
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
opt = 0

# variáveis de operações
soma = 0
mult = 0
maior = 0

while opt != 5:
    
    print("<======= MENU =======>")
    print(
        "[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] sair do programa"
    )
    opt = int(input("escolha uma opção: "))
    
    if opt == 1:
        soma = x + y
        print("Soma de {} + {} = {}".format(x, y, soma))
    
    elif opt == 2:
        mult = x * y
        print("Produto de {} * {} = {}".format(x,y,mult))
    
    elif opt == 3:
        if x > y:
            print("Maior: {}".format(x))
        else:
            print("Maior: {}".format(y))
    
    elif opt == 4:
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))

    elif opt == 5:
        print("Encerrando programa...")
        
    elif opt >= 6:
        print("Opção inválida...")
        
# Bem estruturado