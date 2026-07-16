locadora = []

locadora.append({
    'título':'Star Wars', 
    'ano':1977, 
    'diretor':'George Lucas'
})

locadora.append({
    'título':'Avengers', 
    'ano':2012, 
    'diretor':'Joss Whedon' 
})

locadora.append({
    'título':'Matrix', 
    'ano':1999, 
    'diretor':'Wachowski'
})

print(locadora[0]['ano'])

for i in range(len(locadora)):
    print(locadora[i]['ano'])