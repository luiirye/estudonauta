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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
    
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'Houve um ERRO ao escrever novos dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()