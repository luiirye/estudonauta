# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

## Forma que provavelmente é para ser
x = int(input("Informe um número qualquer"))

print("=" * 30)
print("Forma print a print")
print("{} *  1 = ".format(x), x * 1)
print("{} *  2 = ".format(x), x * 2)
print("{} *  3 = ".format(x), x * 3)
print("{} *  4 = ".format(x), x * 4)
print("{} *  5 = ".format(x), x * 5)
print("{} *  6 = ".format(x), x * 6)
print("{} *  7 = ".format(x), x * 7)
print("{} *  8 = ".format(x), x * 8)
print("{} *  9 = ".format(x), x * 9)
print("{} * 10 = ".format(x), x * 10)
print("=" * 30)

print("=" * 30)
print("Forma utilizando o loop 'for'")

for i in range(1, 10 + 1):
    print("{} * {}" " = ".format(x, i), x * i)
    
print("=" * 30)

# Correto