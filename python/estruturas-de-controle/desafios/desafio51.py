# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))
soma = 0

for i in range(1, 11):
    formula = a +(i -1) * r
    soma += formula  
    print("a{} = {}".format(i,formula))
    
print("SOMA DE TODOS OS TERMOS = {}".format(soma))