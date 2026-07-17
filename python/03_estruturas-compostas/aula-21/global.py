def teste(b):
    global a	
    a = 8 # Essa variável é uma variável local, criada para ser utilizada apenas dentro da função
    b += 4 # O mesmo vale para B e C
    c = 2
	# chama va variável global declarada abaixo
    print(f'A vale {a}')
    print(f'B vale {b}')
    print(f'C vale {c}')

a = 5 # Essa é uma variável GLOBAL, ou seja, ela é lida e válida para o programa todo.
teste(a)
print(f'A fora vale {a}')