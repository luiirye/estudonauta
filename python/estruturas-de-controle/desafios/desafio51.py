# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print("==="*10)
print("     10 TERMOS DE UMA PA     ")
print("==="*10)
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))
soma = 0
decimo_termo = a + (10 - 1) * r

for i in range(a, decimo_termo + r , r):
    formula = a +(i -1) * r
    soma += formula  
    print("a{} = {}".format(i,formula))
    
print("SOMA DE TODOS OS TERMOS = {}".format(soma))