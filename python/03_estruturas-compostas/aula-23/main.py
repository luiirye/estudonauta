try:
    a = int(input(f'Numerador: '))
    b = int(input(f'Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados informados por você')
except ZeroDivisionError:
    print(f'não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print(f'Volte sempre. Muito obrigado!')