# refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher.
# Só que agora, utilizando o laço for
x = int(input("Informe um número para multiplicar: "))
for i in range(1, 11):
    prod = x * i
    print("{} X {:2} = {}".format(x,i,prod))