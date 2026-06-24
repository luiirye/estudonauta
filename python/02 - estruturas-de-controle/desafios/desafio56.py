# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no Final do programa, mostre:

# - A média de idade do grupo.
# - Qual é o nome do Homem mais velho


# variáveis globais

homem_mais_velho_nome = ""
homem_mais_velho_idade = 0
idades = 0
idade_media = 0
menor_mulher = 0


for pessoas in range(1, 5):
    
    # variáveis com entrada pelo usuário
    print("<======== {}ª PESSOA ========>".format(pessoas))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper() # recebe a string, retirando os espaços e transoformando em maiúsculas.
    
    idades += idade
    
    if pessoas == 1 and sexo in 'Mm':
        homem_mais_velho_idade = idade
        homem_mais_velho_nome = nome
    if sexo in 'Mm' and idade > homem_mais_velho_idade:
        homem_mais_velho_idade = idade
        homem_mais_velho_nome = nome
    if sexo in 'Ff' and idade < 20:
        menor_mulher += 1
    
idade_media = idades / 4

    
print("\n<======== ESTATÍSTICAS ========>")
print("A média de idade do grupo é: {}".format(idade_media))
print("O nome do Homem mais velho é: {}".format(homem_mais_velho_nome))
print("Total de mulheres com menos de 20 anos: {}".format(menor_mulher))
    
    