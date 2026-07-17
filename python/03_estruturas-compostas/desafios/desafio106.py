'''
Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM' o programa se encerrará.

OBS: use cores
'''
def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)
    print(f'  {texto}')
    print("~" * tamanho)

def pyhelp(comando):
    help(comando)
    
def loop():
    while True:
        escreva("Sistema de ajuda PyHELP")
        duvida = str(input(f'Digite uma função ou biblioteca: '))
        
        if duvida.lower() == 'fim':
            break
        else:
            escreva(f'Acessando o manual Pyhelp da função/biblioteca {duvida}')
            pyhelp(duvida)
            
loop()