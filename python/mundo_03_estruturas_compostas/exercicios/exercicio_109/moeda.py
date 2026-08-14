def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * (taxa/100))
    return res if formato == False else moeda(preco)

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * (taxa/100))
    return res if formato == False else moeda(preco)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato == False else moeda(preco)

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if formato == False else moeda(preco)

