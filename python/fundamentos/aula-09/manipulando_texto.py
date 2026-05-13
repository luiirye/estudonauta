## Fatiamento
## Fatiando uma string
frase = 'Curso em Vídeo Python'
s = 'prova de python'
print(frase[9]) # Pegando apenas a décima posição da String
print(frase[9:14]) #Começa em 9, e vai até 14, excluindo a posição 14
print(frase[9:21]) #Começa em 9 e vai até a posição 21, ingorando a posição 21 (mesmo não existindo)
print(frase[9:21:2]) # vai de 9 até 21, pulando de 2 em 2
print(frase[:5]) # Sem nada antes do ":", ele começa da posição 0, indo até a posição informada
print(frase[15:]) # começa no 15 sem saber o final, assim indica a partir do 15 até o final da string
print(frase[9::3]) #começa em 9, pulando de 3 em 3 até o final da String. saída: VePh

print(len(s))