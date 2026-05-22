'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA.
MOstrando os 10 primeiros termos da progressão usando a estrutura While.
'''
# Desafio 051 modificado
print("==="*10)
print("10 TERMOS DE UMA PA")
print("==="*10)

# Variáveis da PA
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))
termo = a
count = 1


while count <= 10:
    
    print("{} -> ".format(termo), end = '')
    termo += r # Contador pega o termo e vai somando com a razão # 2 + 3 = 5 + 3 = 8 +3 = ...
    count += 1  
                
print("FIM")