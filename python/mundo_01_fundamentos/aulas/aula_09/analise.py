## função len = length = comprimento
frase = 'Curso em Vídeo Python'
print("=" *50)
print("Função 'Len' ")
print(len(frase))

## Count = contar quantas vezes uma string aparece
print("=" *50)
print("Função 'Count' ")
print(frase.count('o'))
print(frase.count('o',0,13)) #conta quantas letras 'o' a string tem, começando da posição 0 indo até a posição 13 (ignorando a posição 13)

## Find 
print("=" *50)
print("Função 'Find' ")
print("Posição: {}".format(frase.find('deo'))) # Find encontra qual posição está a string solicitada, ou quando começa
print("Posição: {}".format(frase.find('Android'))) # retorna -1, dizendo que a string a ser encontrada não existe na string original

## operador in
print("=" *50)
print("Operador 'in' ")
print('Curso' in frase) # retorna true ou false se tiver ou não

## Replace
print("=" *50)
print("função 'replace' ")
print(frase.replace('Python', 'Android')) ## Substitui a palavra informada pela segunda, não é uma substituição permamente.

## Upper
print("=" *50)
print("função 'Upper' ")
print(frase.upper()) # Transforma todos os caracteres minúsculos da string em maíusculas

## lower
print("=" *50)
print("função 'lower' ")
print(frase.lower()) # Transforma todos os caracteres Maísuculos da string em minúsculas

## capitalize
print("=" *50)
print("função 'capitalize' ")
print(frase.capitalize()) # Joga todos os caracteres para minúsculos, e só o primeiro fica maiúscula

## title
print("=" *50)
print("função 'title' ")
print(frase.title()) # Ele analisa quantas palavras tem a String, identificando pelos espaços. Cada palavra após um espaço, terá a string inicial trocada para maísucula

## Strip
print("=" *50)
print("função 'Strip' ")
frase = '   Aprenda Python  '
print(frase.strip()) ## Remove os espaços do começo e do final da string. tem duas variáveis, rstrip e lstrip. rstrip remove os espaços os espaços da direita, lstrip reomve da esquerda

## Split
frase = 'Curso em Vídeo Python'
print("=" *50)
print("função 'Split'")
print(frase.split()) ## Por padrão, split é feito por espaços, fazendo uma divisão começando pelos espaços criando "pedaços", colocando cada palvra da string em uma nova lista

## Join
print("=" *50)
print("função 'Join'")
print('-'.join(frase)) # Serve para juntar todos os elementos e separar os espaços pelo caractere informado