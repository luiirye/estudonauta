'''
Crie um programa em Python que teste se o site Pudim.com.br está acessível no computador usado.
'''

from urllib import request, error

try:
    # Precisa ter o https ou http para encontrar o site
    site = request.urlopen(f'https://pudim.com.br')
except error.URLError:
    print(f'O site Pudim não pode ser acessado no momento')
else:
    print(f'Consegui acessar o site Pudim com sucesso!')
    print(site.read())