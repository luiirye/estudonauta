def aumentar(n, a):
    aumenta = (n + (n * (a/100)))
    return aumenta

def diminuir(n, a):
    diminui = (n - (n * (a/100)))
    return diminui

def dobro(n):    
    dobra = n * 2
    return dobra

def metade(n):
    metade = n / 2
    return metade 

def moeda(n):
    return f'R$ {n:.2f}'.replace('.' , ',') # troca o ponto por vírgula
    