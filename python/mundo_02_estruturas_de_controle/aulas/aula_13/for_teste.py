# n = int(input("Digite um número: "))

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

for c in range(inicio, fim + 1, passo):
    print(c)
print("Fim")
# Pede ao usuário informar um número>
# Após informar, o loop For conta até o número informado pelo usuário.
# n + 1 porq o último número é ignorado pelo loop

print("SOMATÓRIO COM FOR")
s = 0
for x in range(0,4):
    n = int(input("DIgite um valor: "))
    s += n
print("O SOMATÓRIO de s = {}".format(s))
print("FIM")