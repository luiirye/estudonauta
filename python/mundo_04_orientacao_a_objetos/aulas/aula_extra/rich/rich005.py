from rich.traceback import install

install() # -> Função para deixar os erros mais visualmente bonitos e entendíveis

def divisao(x, y):
    return x / y

print(divisao(50,0))