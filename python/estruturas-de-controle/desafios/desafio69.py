'''
Crie um programa que leia a idade e o sexo de várias pessoas.

A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

No final, mostre:
    A) Quantas pessoas tem mais de 18 anos
    B) Quantos HOMENS foram cadastrados
    C) Quantas MULHERES tem menos de 20 anos
'''



while True:
    
    nome = str(input("Informe o nome da pessoa: "))
    idade = int(input("Informe a idade dessa pessoa: "))
    sexo = str(input("Informe o sexo dessa pessoa: "))
    if sexo not in 'MmFf': 
        while True:
            print("Sexo inválido. Digite apenas [M/F]")
            sexo = str(input("Informe o sexo dessa pessoa: "))
                
    opt = str(input("Quer continuar? [S/N]: "))    
    
    if opt not in 'Ss':
        print("\n")
        nome = str(input("Informe o nome da pessoa: "))
        idade = int(input("Informe a idade dessa pessoa: "))
        sexo = str(input("Informe o sexo dessa pessoa: "))
        if sexo not in 'MmFf':
            while True:
                print("Sexo inválido. Digite apenas [M/F]")
                sexo = str(input("Informe o sexo dessa pessoa: "))
            
        opt = str(input("Quer continuar? [S/N]: "))
        
    else:
        print("Programa encerrado...")
        break

print("\n")
print("Quantidade de pessoas com mais de 18 anos: {}")
print("Quantidade de Homens cadastrados: {}")
print("Quantidade de Mulheres com menos de 20 anos cadastradsa: {}")