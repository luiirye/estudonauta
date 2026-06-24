# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print("==="*5)
print("GERADOR DE PA")
print("==="*5)

# Variáveis da PA
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))
termo = a
count = 1
total = 0
mais = 10

while mais != 0:
    
    total += mais
    
    while count <= total:
        
        print("{} -> ".format(termo), end = '')
        termo += r # Contador pega o termo e vai somando com a razão # 2 + 3 = 5 + 3 = 8 +3 = ...
        count += 1  
                    
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print('FIM.\nProgressão finalizada com {} termos mostrados.'.format(total))