# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média acima de 7.0: APROVADO

print("-=-" * 10)
print(" CALCULO DE MÉDIA ")
print("-=-" * 10)

n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))

media = (n1 + n2) / 2

if(media < 5.0):
    print("Média: {:.1f}\nReprovado.".format(media))
elif (media > 5.0 and media <=6.9):
    print("Média: {}\nRecuperação.\nBora estudar!!".format(media))
else:
    print("Média: {}\nAPROVADO!!\nParabéns!!".format(media))