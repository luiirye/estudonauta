def contador(i,f,p):
    '''
    -> Faz uma contagem e mostra na tela.
    i = parâmetro que recebe o início da contagem.
    f = parâmetro que recebe o fim da contagem.
    p = parâmetro que recebe o passo da contagem.
    return = returna um resultado. (Nesse caso, não tem)
    
    Função criada por Luii
    '''
    c = i
    while c <= f:
        print(f'{c}', end ='')
        c += p
    print(f'FIM!')
    
help(contador)
    