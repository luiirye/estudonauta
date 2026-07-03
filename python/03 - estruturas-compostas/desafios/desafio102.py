'''
Cria uma função fatorial().
Ela receberá dois parâmetros: o primeiro que indique o número a calcular e o outro chamado SHOW.
SHOW será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo fatorial.
'''
def imprimir_fatorial(n):
    if n < 0:
        return "Fatorial não existe para números negativos."
    if n == 0 or n == 1:
        return f"{n}! = 1"
    
    fatorial = 1
    passos = []
    
    for i in range(n, 0, -1):
        fatorial *= i
        passos.append(str(i))
    
    calculo_extenso = " x ".join(passos)
    
    print(f"{n}! = {calculo_extenso} = {fatorial}")

def fatorial(n, show=False):
    if n < 0:
        return f'Não existe fatorial de números negativos'
    if n == 0 or n == 1:
        return f'{n}! = 1'
    
    f = 1
    for c in range(n, 0 ,-1):
        f *= c
    
    if show == True:
        return imprimir_fatorial(n)
    else:
        return f'{f}'
    
print(f'{fatorial(5, show=False)}\n{fatorial(5, show=True)}')

