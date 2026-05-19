# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de idade.
# Considere maior idade como 21 anos.

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for pessoas in range(1,8):

    ano = int(input("Informe o ano em que a {}ª pessoa nasceu: ".format(pessoas)))
    idade = ano_atual - ano

    if (idade < 21):
        menor += 1
    else:
        maior += 1
        
print("{} pessoas ainda NÃO atingiram a maioridade.\n{} pessoas são maoires de idade.".format(menor, maior))