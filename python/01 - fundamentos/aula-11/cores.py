print("\033[1;31;43mOlá, mundo\033[m") #\033 [ Negrito ;texto vermelho ; fundo vermelho \033 [m para fechar
print("\033[4;30;45mOlá, mundo\033[m") #\033 [ sublinhado ;texto branco ; fundo mangeta \033 [m para fechar
print("\033[7;33;44mOlá, mundo\033[m") # Invertendo as cores

a = 3
b = 5
print('Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m!!!'.format(a, b))