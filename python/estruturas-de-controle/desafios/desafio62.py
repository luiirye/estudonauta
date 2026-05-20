# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print("==="*10)
print("     10 TERMOS DE UMA PA     ")
print("==="*10)

# Variáveis da PA
a = int(input("Informe o primeiro termo: "))
r = int(input("Informe a razão: "))

dec_trm = (a + (10 - 1) * r)

count = a
ai = 1 
soma = 0

while count <= dec_trm:
    
    print("a{} -> {}".format( ai, count))
    count += r  # Contador pega o termo e vai somando com a razão
                # 2 + 3 = 5 + 3 = 8 +3 = ...
    ai += 1     # Para ilustrar qual "an" está
    
    if count == dec_trm:
        print("Gostaria de mostrar mais algum termo?\n")
        resp = str(input("[Sim] / [Não] : ")).strip().upper()
        
        if resp == 'SIM':
            a = int(input("Informe o primeiro termo: "))
            r = int(input("Informe a razão: "))
            dec_trm = (a + (10 - 1) * r)
            cont = a
            
        else: 
            print("Encerrando programa...")