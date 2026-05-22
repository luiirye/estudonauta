'''
Crie um programa que leia vários números inteiros pelo teclado.

O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 

No final, mostre:
    - Quantos números foram digitados
    - Qual foi a soma entre eles (desconsiderando o flag(999))
'''
n = soma = count =0
'''
é o equivalente á:
n = 0
soma = 0
count = 0
'''

while n != 999:
    
    # leitura dos números
    n = int(input("Informe um número inteiro qualquer [999 para parar]: "))
    
    if n == 999:
        soma -= 999
        count -= 1
    
    count += 1 
    soma += n
    
print("Você digitou {} números e a soma = {}.".format(count, soma))