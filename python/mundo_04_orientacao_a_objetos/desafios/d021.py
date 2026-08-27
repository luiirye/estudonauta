class Caneta:
    def __init__(self):
        
        # Atributos para utilizar uma caneta
        
        self.pegar = False
        self.largar = False
        self.tampa = True
        self.destampa = False
        self.cor = ["Preto", "Azul", "Vermelho", "Verde", "Roxo"]
        self.tinta = 100
        self.escrever = False
     
     
    # Métodos para utilizar uma caneta
    
    def pegar_caneta(self):
        # Primeiro, ṕreciso pegar uma caneta para poder escrever
        if self.pegar == False:
            print(f'Opa, peguei uma caneta!!')
            return self.pegar == True
        
        else:
            print(f'Já estou com a caneta na mão!')
            return self.pegar == True

# Objetos da Classe Caneta
