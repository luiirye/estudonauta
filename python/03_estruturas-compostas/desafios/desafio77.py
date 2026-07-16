'''
CRie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois, você deve mostrar para cada palavra, quais são suas VOGAIS
'''
palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro'
)

vogais = 'aeiou'

for palavra in range(0, len(palavras)):
    
    print(f"\nNa palavra {palavras[palavra]} temos as vogais: ", end='')
    
    for vogal in palavras[palavra]:
        
        if vogal in vogais:
            print(vogal, end ='')