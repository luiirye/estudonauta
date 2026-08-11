from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho(f'opção 2')
    elif resposta == 3:
        cabecalho(f'Saindo do sistema... Até logo!!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)