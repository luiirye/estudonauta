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
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input(f'Nome: '))
        idade = leiaInt(f'Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho(f'Saindo do sistema... Até logo!!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2) 