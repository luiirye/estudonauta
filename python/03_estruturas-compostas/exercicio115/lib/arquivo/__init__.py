from lib.interface import *

def arquivoExiste(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Ouve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome }')
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'ERRO ao abrir o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.readlines())
    