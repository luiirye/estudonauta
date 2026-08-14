# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o MAIOR e o MENOR peso lidos.

maior = 0
menor = 0

for pessoas in range (1, 6):
    pesos = float(input("Informe o peso da {}ª pessoa: ".format(pessoas)))
    
    if pessoas == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos
        
    
print("A pessoa com {:.1f}Kg tem o MAIOR peso".format(maior))
print("A pessoa com {:.1f}Kg tem o MENOR peso".format(menor))
    