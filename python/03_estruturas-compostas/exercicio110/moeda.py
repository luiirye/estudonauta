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

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def resumo(preco, taxaa = 10, taxar = 10):
    print(f'-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print(F'-' * 30)

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print(F'-' * 30)