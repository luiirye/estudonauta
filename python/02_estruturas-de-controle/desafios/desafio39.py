# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

print("-=-" * 15)
print("\033[0;36;00m ALISTAMENTO MILITAR \033[m")
print("-=-" * 15)


ano = int(input("Informe o seu ano de nascimento: "))
ano_atual = date.today().year
idade = (ano_atual - ano)
dif = (ano_atual - ano - 18)

if (idade == 18):
    print("Idade: {}\nHora de se alistar.".format(idade))
elif (idade > 18):
    print("Idade: {}\nJá passou da hora de se alistar.\nfaz(em) {} anos do tempo de alistamento.".format(idade, dif))
elif (idade < 18):
    print("Idade: {}\nFaltam {} anos para se alistar".format(idade, dif))