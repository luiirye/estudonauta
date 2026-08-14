adicao = "+"
subtracao = "-"
multiplicacao = "*"
potencia = "**"
divisao = "/"
divisao_inteira = "//"
incremento = "++"
soma_valor_igual = "+="
sub_valor_igual = "-="
atribuicao = "=="
resto = "%"

# ordem de procedência
# primeiro ()
# segundo **
# terceiro * / // %
# quarto + -

teste1 = (5 + 3 * 2)
teste2 = (3 * 5 + 4 ** 2)
teste3 = (3 * (5 + 4) ** 2)

print(teste1)
print(teste2)
print(teste3)

n1 = int(input("Digite um valor"))
n2 = int(input("Digite outro valor"))

# Aplicando operações aritméticas com os números
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
exp = n1 ** n2

print(
    'A soma é {},\n a subtração é {},\n o produto é {},\n a divisão é {:.3f}'.format(soma, sub, mult, div), end='\n'
)
print(
    'Divisão inteira {} e potência {}'.format(div_int, exp)
)