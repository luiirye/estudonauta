'''
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# ==========================
# Passo 1: Estrutura do pacote utilidadesCeV
# Simulado em um único arquivo para a atividade
# ==========================

# ==========================
# Passo 2: módulo moeda.py
# ==========================
'''

from utilidadesCeV.moedas.moedas import resumo

valor = float(input(f'Digite o preço: R$ '))
taxa_aumento = float(input(f'Digite a porcentagem de aumento para R$ {valor:.2f}: '))
taxa_reduz = float(input(f'Digite a porcentagem de aumento para R$ {valor:.2f}: '))

resumo(valor, taxa_aumento, taxa_reduz)