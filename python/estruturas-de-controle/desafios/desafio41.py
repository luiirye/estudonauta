# Leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 20 anos: SÊNIOR
# - acima: MASTER 

from datetime import date

ano_nascimento = int(input("Informe o ano de nascimento do atleta: "))
atual = date.today().year
idade = (atual - ano_nascimento)

if (idade <= 9):
    print("Idade: {}.\nMIRIM".format(idade))
elif (idade > 9 and idade <= 14):
    print("Idade: {}.\nINFANTIL".format(idade))
elif (idade > 14 and idade <= 19):
    print("Idade: {}.\nJUNIOR".format(idade))
elif (idade > 19 and idade == 20):
    print("Idade: {}.\nSÊNIOR".format(idade))
else:
    print("Idade: {}.\nMASTER".format(idade))