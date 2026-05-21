# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print("==="*10)
print("     10 TERMOS DE UMA PA     ")
print("==="*10)

# Variáveis da PA
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))

count = a # Valor atual da PA
ai = 1 # contador de termos

mais = 10 # começa mostrando 10 termos
total = 0 # total de termos mostrados

while mais != 0:
    
    total += mais

    while ai <= total: # enquanto os termos forem menores ou iguais ao total de termos, faça o bloco
        print("a{} -> {}".format(ai, count))
        
        count += r
        ai += 1
        
    mais = int(input("Quer mostrar mais quantos termos?"))
    
print("Encerrando programa...'")
        