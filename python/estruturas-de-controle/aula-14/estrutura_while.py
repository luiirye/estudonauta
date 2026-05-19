print("<=== FOR ===>") # é utilizado quando SE SABE o limite do bloco
for c in range(1, 5):
    n = int(input("Digite um valor"))
print('Fim')

print("<=== WHILE ===>")

r = 'S'
while r == 'S': # é utilizado quando NÃO SE SABE o limite do bloco
    x = int(input("Digite um valor: "))
    r = str(input("Quer continuar?[S/N]: ")).upper()
print('Fim')