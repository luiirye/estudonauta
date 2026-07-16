def moeda(n):
    return f'R$ {n:.2f}'.replace('.' , ',') # troca o ponto por vírgula

def aumentar(n = 0, a = 0, formato = False):
    
    aumenta = (n + (n * (a/100)))
    
    if formato == True:
        return moeda(aumenta)
    else:
        return aumenta

def diminuir(n = 0, a = 0, formato = False):
    
    diminui = (n - (n * (a/100)))
    
    if formato == True:
        return moeda(diminui)
    else:
        return diminui

def dobro(n = 0, formato = False):    
    
    dobra = n * 2
    
    if formato == True:
        return moeda(dobra)
    else:
        return dobra

def metade(n = 0, formato = False):
    metade = n / 2
    
    if formato == True:
        return moeda(metade)
    else:
        return metade 
    
def resumo(numero = 0 , taxa_aumento = 0, taxa_reducao = 0):
    print(f'-' * 30)
    print(F'RESUMO DO VALOR'.center(30))
    print(f'-' * 30)

    print(f'A metade de {moeda(numero)} é {metade(numero, True)}')
    print(f'O dobro de {moeda(numero)} é {dobro(numero, True)}')
    print(f'Aumentando em {taxa_aumento}%, temos {aumentar(numero, 10, True)}')
    print(f'Reduzindo em {taxa_reducao}%, temos {diminuir(numero, 13, True)}')