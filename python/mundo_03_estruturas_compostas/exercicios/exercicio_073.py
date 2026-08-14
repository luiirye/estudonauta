'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois, mostre:
    a) Apenas o 5 primeiros colocados
    b) Os últimos 4 da colocação da tabela
    c) Uma lista com os times em ordem alfabética
    d) Em que posição na tabela está o time Chapecoense
'''
brasileirao = (
    "Palmeiras",
    "Flamengo",
    "Fluminense",
    "Athletico-PR",
    "RB Bragantino",
    "Coritiba",
    "São Paulo",
    "Bahia",
    "Cruzeiro",
    "Botafogo",
    "Vitória",
    "Atlético-MG",
    "Internacional",
    "Grêmio",
    "Vasco da Gama",
    "Corinthians",
    "Santos",
    "Mirassol",
    "Remo",
    "Chapecoense"
)

print('-=' * 15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=' * 15)

# a) Mostrar os 5 primeiros colocados.
print("-=" * 15)
print("Os 5 primeiros da tabela: ")
print(brasileirao[0:5])

# b) mostra os últimos quatro da tabela
print("-=" * 15)
print("Os 4 últimos da tabela: ")
print(brasileirao[-4:]) # começa em 16 : vai até 20 : anda de um em um

# c) uma lista em ordem alfabética
ordem_alf = sorted(brasileirao)
print("-=" * 15)
print(ordem_alf)

# d) Exibir a posição da chapecoense
print("-=" * 15)
print("Posição do time Chapecoense na tabela: ", end = '')
for i in range(0, len(brasileirao)):
    if brasileirao[i] == 'Chapecoense': #Se o contador na tupla for igual á "Chapecoense", exibirá sua posição.
        print(i+1)