# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de idade.
# Considere maior idade como 21 anos.

for i in range(1, 8, 1):
    ano = int(input('informe o ano de nascimento da pessoa {}: ').format(i))

print(ano, end = '')    
