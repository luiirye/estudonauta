from math import ceil # Arredondar para cima
from math import floor # Arredondar para baixo
from math import trunc # Truncate, eliminar um número da vírgula para frente
from math import pow # Exponenciação
from math import sqrt # raíz quadrada
from math import factorial # cálculo de fatorial

num = int(input("Digite um número: "))
trunc_test = 3.14118284901414819024981409124

# Raiz quadrada
raiz = sqrt(num)

print("A raiz de {} é {}".format(num, raiz))
print("A raiz de {} é {} (Arredondada para cima)".format(num, ceil(raiz)))
print("A raiz de {} é {} (Arredondada para baixo)".format(num, floor(raiz)))
print("Eliminando números após a vírgula. Sem trunc: {}. Com trunc: {}".format(trunc_test, trunc(trunc_test)))
print("Exponenciação de 2 de {} = {}".format(num, pow(num, 2)))
print("Fatorial de {} = {}".format(num, factorial(num)))
